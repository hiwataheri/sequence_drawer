What is the Sequence Drawer
=========================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Introduction
#############################

The Sequence Drawer is an app, that generates a SMILES String into an 2D image of the molecular structure of this SMILES.

Technologies used
###################

For this simple app, the following packages where used:

* rdKit
* ImageTK
* cv2
* numpy

This is my code for the applayer::

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

