import argparse
from os import listdir, remove
from os.path import isdir, join, isfile
import subprocess
import filecmp
import shutil
import time
import pytest


STANZA_EXT= ".stanza"
BOARD_IMAGE= "board.svg"
SCHEMATIC_IMAGE= "schematic.svg"

def comp_dir(dir1, dir2):
    dirs_cmp = filecmp.dircmp(dir1, dir2)
    if len(dirs_cmp.left_only)>0 or len(dirs_cmp.right_only)>0 or \
        len(dirs_cmp.funny_files)>0:
        return False
    (_, mismatch, errors) =  filecmp.cmpfiles(dir1, dir2, dirs_cmp.common_files, shallow=False)
    if len(mismatch)>0 or len(errors)>0:
        return False
    for common_dir in dirs_cmp.common_dirs:
        sub_dir1 = join(dir1, common_dir)
        sub_dir2 = join(dir2, common_dir)
        if not comp_dir(sub_dir1, sub_dir2):
            return False
    return True

def run_stanza_file(dir, file):
    command = "cd " + dir + " ; jitx run " + file
    try: 
        test_case = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        jitx_output = test_case.stdout
        # print(jitx_output)
    except subprocess.CalledProcessError as err:
        pytest.fail("command '{}' return with error (code {}): {}".format(err.cmd, err.returncode, err.output))

def get_output_dir(test_dir):
    if isfile(join(test_dir,"board.svg")):
        return join(test_dir,"board.svg")
    else:
        return join(test_dir,"schematic.svg")

def get_main_filename(test_dir, test_case):
    input_dir= listdir(join(test_dir, "input"))
    if "kicad" in test_case:
        files = [item for item in input_dir if item.endswith(".kicad_pcb")]
        return files[0].split(".")[0]+ STANZA_EXT if files else "KicadProject.stanza"
    elif "altium" in test_case:
        files = [item for item in input_dir if item.endswith("(PRJPCB).JSON")]
        return files[0].split("(")[0]+ STANZA_EXT if files else None

def generate_and_verify_views(test_dir, mainfile):
    run_stanza_file(test_dir, mainfile)
    try:
        assert filecmp.cmp(join(test_dir, BOARD_IMAGE), join(test_dir, "expected-board.svg")), "Board view is incorrect"
        assert filecmp.cmp(join(test_dir, SCHEMATIC_IMAGE), join(test_dir, "expected-schematic.svg")), "Scematic view is incorrect"
    except FileNotFoundError:
        pytest.fail("Views are not generated")

def run_and_verify(test_dir):
    
    assert isdir(test_dir), "No such directory exists: {}".format(test_dir)

    out_schematic = get_output_dir(test_dir)
    # Deleting output directory if already exists
    if isfile(out_schematic):
        remove(out_schematic)    
    # Running test stanza file
    # start= time.time()
    files = [item for item in listdir(test_dir) if item.endswith(STANZA_EXT)]

    if files:
        generate_and_verify_views(test_dir, files[0])
    else:
        pytest.fail("No test stanza file found")
        return
    """
    #Verify and compare output directory
    actual_output_dir= get_output_dir(test_dir)
    expected_output_dir= join(test_dir, "expected-output")

    assert isdir(actual_output_dir), "Output not generated"
    assert comp_dir(actual_output_dir, expected_output_dir), "Output directory doesn't match"

   

     # Get main stanza file name
    mainfile= get_main_filename(test_dir, test_case)
    if not mainfile:
        pytest.fail("Main stanza file is not generated")
    else:
        print("Output is correct")    
    """
    
    
