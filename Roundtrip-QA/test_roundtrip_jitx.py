"""This file contains the Roundtrip QA test cases"""
import pytest
import test_utility

# Methods to execute the Roundtrip QA test cases
def test_kicad_3d():
    test_utility.run_and_verify("test-kicad-3d")

def test_kicad_add_3d():
    test_utility.run_and_verify("test-kicad-add-3d")
