"""This file contains the methods required for executing the Roundtrip QA test cases"""
from os import listdir
from os.path import isdir, join, dirname, abspath
import subprocess
import shutil
import logging
import sys
import platform
import pytest

# To import file from parent directory
sys.path.append("../")
from utility_methods import comp_dir, get_output_dir

# Constants
STANZA_EXT= ".stanza"
BOARD_IMAGE= "board.svg"
SCHEMATIC_IMAGE= "schematic.svg"

# Path of stanza.proj file
OCDB_PATH = join(join(dirname(dirname(abspath(__file__))),"ocdb"),"stanza.proj").replace('\\','/')

def run_stanza_file(directory, file):
    """
    Runs the given stanza file
    :param directory: Path of the directory containing the stanza file
    :param file: Name of the stanza file
    """
    if platform.system() == "Windows":
        command = "cd " + directory + "\n"+ "jitx run " + file+"\n"
        try:
            process = subprocess.Popen( "cmd.exe", shell=False, universal_newlines=True,
                    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate(command)
            return out
        except subprocess.CalledProcessError as err:
            pytest.fail("command '{}' return with error (code {}): {}".format(
                err.cmd, err.returncode, err.output))
    else:
        command = "cd " + directory + " ; jitx run " + file
        try:
            test_case = subprocess.run(command, shell=True, stdout=subprocess.PIPE, \
                                                    stderr=subprocess.PIPE, text=True, check=True)
            jitx_output = test_case.stdout
            return jitx_output
        except subprocess.CalledProcessError as err:
            pytest.fail("command '{}' return with error (code {}): {}".format(
                err.cmd, err.returncode, err.output))

def get_main_filename(output):
    """
    Returns the name of the stanza file
    :param output: Console output
    :return: Name of the stanza file
    """
    arr = output.split(" ")
    temp = arr[-1]
    if platform.system() == "Windows":
        temp = temp.split("\n")[0]
    else:
        temp = temp.replace("\n","")
    return temp

def run_and_verify(test_dir):
    """
    Executes the test case steps and verifies the output directory
    :param test_dir: Path of the test directory
    """
    assert isdir(test_dir), "No such directory exists: {}".format(test_dir)
    outdir= get_output_dir(test_dir)

    # Deleting output directory if already exists
    if isdir(outdir):
        shutil.rmtree(outdir)

    # Running test stanza file
    files = [item for item in listdir(test_dir) if item.endswith(STANZA_EXT)]
    if files:
        console_output = run_stanza_file(test_dir, files[0])
    else:
        pytest.fail("No test stanza file found")
        return

    if test_dir == "test-kicad-add-3d":
        # Adding ocdb component to stanza.proj file
        try:
            temp = open(join(outdir, "stanza.proj"), "a")
            cmd = ["include \""+OCDB_PATH+"\""]
            temp.writelines(cmd)
            temp.close()
        except Exception as err:
            pytest.fail("Could not find stanza.proj file." + str(err))
        main_file_name = get_main_filename(console_output)
        temp_dir = test_dir + "/output/" + main_file_name
        with open(temp_dir, "r") as file1:
            contents = file1.readlines()

        contents.insert(88, "  val keycap = ocdb/scripts/kle-importer/KeyCap(0, 0, [0.0, 0.0], [], \
            Rectangle(1.0, 1.0)) \n  inst SW1 : ocdb/cherry/MX/component(keycap) \n")

        with open(temp_dir, "w") as file1:
            contents = "".join(contents)
            file1.write(contents)

        file_dir = test_dir + "/output/"
        if main_file_name:
            console_output = run_stanza_file(file_dir, main_file_name)
        else:
            pytest.fail("No test stanza file found")
            return

        if platform.system() == "Windows":
            command = "cp " + test_dir + "/kailh_socket_mx.stp " + test_dir + "/output/jitx-design/3d-models/ " + "\n"
            try:
                process = subprocess.Popen( "cmd.exe", shell=False, universal_newlines=True,
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = process.communicate(command)
            except subprocess.CalledProcessError as err:
                pytest.fail("command '{}' return with error (code {}): {}".format(
                    err.cmd, err.returncode, err.output))
        else:
            command = "cp " + test_dir + "/kailh_socket_mx.stp " + test_dir + "/output/jitx-design/3d-models/ "
            try:
                subprocess.run(command, shell=True, stdout=subprocess.PIPE,
                                            stderr=subprocess.STDOUT, text=True, check=True)
            except subprocess.CalledProcessError as err:
                logging.error(err.output)
                pytest.fail("Test case failed with error "+ err.output)

    else:
        # Verify and compare output directory
        actual_output_dir= get_output_dir(test_dir)
        if platform.system() == "Windows":
            expected_output_dir= join(test_dir, "expected-output-import-win")
        else:
            expected_output_dir= join(test_dir, "expected-output-import")
        main_file_name = get_main_filename(console_output)
        assert isdir(actual_output_dir), "Import Output not generated"
        assert comp_dir(actual_output_dir, expected_output_dir), \
            "Import Output directory doesn't match"

        if main_file_name:
            temp_dir = test_dir + "/output"
            console_output = run_stanza_file(temp_dir, main_file_name)
        else:
            pytest.fail("No test stanza file found")
            return

        actual_output_dir_export= get_output_dir(test_dir)
        if platform.system() == "Windows":
            expected_output_dir_export= join(test_dir, "expected-output-export-win")
        else:
            expected_output_dir_export= join(test_dir, "expected-output-export")

        assert isdir(actual_output_dir_export), "Export Output not generated"
        assert comp_dir(actual_output_dir_export, expected_output_dir_export), \
            "Export Output directory doesn't match"
