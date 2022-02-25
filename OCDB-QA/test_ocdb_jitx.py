"""This file contains the OCDB QA test cases"""
import pytest
import test_utility

# Methods to execute the OCDB QA test cases
def test_mpn_core():
    test_utility.run_and_verify("test-mpn-core")

def test_replaced_microcontroller():
    test_utility.run_and_verify("test-replaced-microcontroller")
