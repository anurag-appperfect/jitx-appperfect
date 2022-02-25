"""This file contains the methods required for executing the OCDB QA test cases"""
from os import listdir, remove
from os.path import isdir, join, isfile, exists
import filecmp
import shutil
import sys
import platform
import pytest

# To import file from parent directory
sys.path.append("../")
from utility_methods import run_stanza_file

# Constants
STANZA_EXT= ".stanza"
BOARD_IMAGE= "board.svg"
SCHEMATIC_IMAGE= "schematic.svg"

def get_view_file(test_dir, mainfile):
    """
    Returns the svg file for board/schematic view
    :param test_dir: Path of the test directory
    :return: Path of the view file
    """
    if isfile(join(test_dir, mainfile+"-board.svg")):
        return join(test_dir, mainfile+"-board.svg")
    else:
        return join(test_dir, mainfile+"-schematic.svg")

def generate_and_verify_views(test_dir, mainfile):
    """
    Generates board and schematic views and verifies them with the expected views
    :param test_dir: Path of the test directory
    :param mainfile: Name of the stanza file
    """
    run_stanza_file(test_dir, mainfile)
    mainfile_name = mainfile.split(".")[0]
    if platform.system() == "Windows":
        expected_board = "expected-" + mainfile_name+ "-win-"+ BOARD_IMAGE
        expected_schematic = "expected-" + mainfile_name+ "-win-"+ SCHEMATIC_IMAGE
    else:
        expected_board = "expected-" + mainfile_name+ "-"+ BOARD_IMAGE
        expected_schematic = "expected-" + mainfile_name+ "-"+ SCHEMATIC_IMAGE
    generated_board = mainfile_name + "-" + BOARD_IMAGE
    generated_schematic = mainfile_name + "-" + SCHEMATIC_IMAGE
    try:
        assert filecmp.cmp(join(test_dir, generated_board), \
            join(test_dir, expected_board)), "Board view is incorrect"
        assert filecmp.cmp(join(test_dir, generated_schematic), \
            join(test_dir, expected_schematic)), "Scematic view is incorrect"
    except FileNotFoundError:
        arr = [join(test_dir, generated_board), join(test_dir, expected_board), \
            join(test_dir, generated_schematic), join(test_dir, expected_schematic)]
        for file in arr:
            if exists(file) is False:
                if "expected" not in file:
                    pytest.fail("Views are not generated")
                else:
                    pytest.fail("Expected Views are not present")

def run_and_verify(test_dir):
    """
    Executes the test case steps and verifies the output directory
    :param test_dir: Path of the test directory
    """
    assert isdir(test_dir), "No such directory exists: {}".format(test_dir)
    if isdir("jitx-design"):
        shutil.rmtree("jitx-design")

    # Running test stanza file
    files = [item for item in listdir(test_dir) if item.endswith(STANZA_EXT)]
    if files:
        for i in range(len(files)):
            out_board = get_view_file(test_dir,files[i].split(".")[0])
            # Deleting output directory if already exists
            if isfile(out_board):
                remove(out_board)

            out_schematic = get_view_file(test_dir,files[i].split(".")[0])
            # Deleting output directory if already exists
            if isfile(out_schematic):
                remove(out_schematic)

            generate_and_verify_views(test_dir, files[i])
    else:
        pytest.fail("No test stanza file found")
        return
