"""
Unit and regression test for the sequence_drawer package.
"""

# Import package, test suite, and other packages as needed
import sequence_drawer
from .compare_images import compare_images_task
import pytest
import sys
import os
from pathlib import Path

HERE = Path(__file__).parent


def test_sequence_drawer_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "sequence_drawer" in sys.modules


def test_compare_test_image():
    original = HERE / "data/test_image.png"
    duplicate = HERE / "data/pictureofmolecule.png"
    assert compare_images_task(original, duplicate)


@pytest.mark.parametrize(
    "smiles, expected_image",
    [
        (
            "CC(C)c1c(C(=O)Nc2ccccc2)c(c(c3ccc(F)cc3)n1CC[C@@H]4C[C@@H](O)CC(=O)O4)c5ccccc5",
            HERE / "data/test_image.png",
        )
    ],
)
def test_smiles_to_image(smiles, expected_image):
    image = sequence_drawer.convert_smiles_to_image(smiles)
    assert compare_images_task(image, expected_image)
    os.unlink(image)
