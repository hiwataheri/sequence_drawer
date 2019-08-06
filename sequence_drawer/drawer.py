"""
drawer.py
Create a 2D drawing out of a SMILES input.

Convention for naming:
Functions and Variables = lower_case_with_underscores
"""
from rdkit import Chem
from rdkit.Chem import Draw
from .applayer import command_parser


def convert_smiles_to_image(smiles, path="image.png"):
    user_smiles = Chem.MolFromSmiles(smiles)
    image_of_user_molecule = Draw.MolToFile(user_smiles, path, size=(900, 900))
    return path
