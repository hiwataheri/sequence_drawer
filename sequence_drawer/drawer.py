"""
drawer.py
Create a 2D drawing out of a SMILES input.

Handles the primary functions
"""
from rdkit import Chem
from rdkit.Chem import Draw
from applayer import commandparser
import argparse

def convert_SMILES_to_Image():
    parser = argparse.ArgumentParser(description='Parse 2D View')
    parser.add_argument('user_input_smile')
    args = parser.parse_args()
    s=args.user_input_smile
    drawthis=Chem.MolFromSmiles(s)
    image_of_user_molecule = Draw.MolToFile(drawthis,'./data/pictureofmolecule.png', size=(900,900))
    return image_of_user_molecule


'''if __name__ == "__main__":
    convert_SMILES_to_Image()'''