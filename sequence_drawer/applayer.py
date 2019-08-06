"""
applayer.py
Get's Input as a SMILES from the User and gives back a 2D Picture 
generated with drawer.py
"""
import argparse
import tkinter as tk
from PIL import ImageTk, Image


def command_parser():
    parser = argparse.ArgumentParser(description="Parse 2D View")
    parser.add_argument("smiles")
    args = parser.parse_args()
    smiles = args.smiles
    return smiles


def display(title="Your molecule", geometry="900x900"):
    window = tk.Tk()
    window.title(title)
    window.geometry(geometry)
    window.configure(background="white")
    window_img = ImageTk.PhotoImage(Image.open("./data/pictureofmolecule.png"))
    panel = tk.Label(window, image=window_img)
    panel.image = window_img
    panel.pack(side="bottom", fill="both", expand="yes")
    window.mainloop()


if __name__ == "__main__":
    smiles = command_parser()
    import drawer

    drawer.convert_smiles_to_image(smiles)
    display()
