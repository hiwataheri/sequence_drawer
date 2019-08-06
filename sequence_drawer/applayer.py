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


def display(
    title="Your molecule",
    geometry="900x900",
    background="white",
    path="./data/pictureofmolecule.png",
    image="ph",
    side="bottom",
    fill="both",
    expand="yes",
):
    window = tk.Tk()
    window.title(title)
    window.geometry(geometry)
    window.configure(background)
    window_img = Image.open(path)
    ph = ImageTk.PhotoImage(window_img)
    panel = tk.Label(window, image)
    panel.image = ph
    panel.pack(side, fill, expand)
    window.mainloop()
    return 1


if __name__ == "__main__":
    smiles = command_parser()
    import drawer

    drawer.convert_smiles_to_image(smiles)
    display()
