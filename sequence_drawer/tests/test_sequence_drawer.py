"""
Unit and regression test for the sequence_drawer package.
"""

# Import package, test suite, and other packages as needed
import sequence_drawer
from compare_images import compare_images_task
import pytest
import sys
from sequence_drawer import applayer



def test_sequence_drawer_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "sequence_drawer" in sys.modules

def test_applayer():
	applayer 'CC(C)c1c(C(=O)Nc2ccccc2)c(c(c3ccc(F)cc3)n1CC[C@@H]4C[C@@H](O)CC(=O)O4)c5ccccc5' 

def test_compare_test_image():
    assert compare_images_task() == 1
