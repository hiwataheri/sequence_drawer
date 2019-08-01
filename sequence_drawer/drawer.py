"""
drawer.py
Create a 2D drawing out of a SMILES input.

Convention for naming:
Functions = CapitalizedWords
Variables lower_case_with_underscores
"""
from rdkit import Chem
from rdkit.Chem import Draw
from applayer import CommandParser


def ConvertSmilesToImage(smiles):
    draw_this = Chem.MolFromSmiles(smiles)
    image_of_user_molecule = Draw.MolToFile(
        draw_this, "./data/pictureofmolecule.png", size=(900, 900)
    )
    return image_of_user_molecule
