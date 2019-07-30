import argparse
import tkinter as tk
from PIL import ImageTk, Image


def commandparser():
	parser = argparse.ArgumentParser(description='Parse 2D View')
	parser.add_argument('smile')
	args = parser.parse_args()
	smiles=args.smile
	return smiles

def display():
	window=tk.Tk()
	window.title("Your molecule")
	window.geometry("900x900")
	window.configure(background="white")
	windowimg = Image.open('./data/pictureofmolecule.png')
	ph = ImageTk.PhotoImage(windowimg)
	panel = tk.Label(window,image=ph)
	panel.image = ph
	panel.pack(side="bottom", fill="both",expand="yes")
	window.mainloop()

if __name__ == '__main__':
	smiles = commandparser()
	import drawer
	drawer.convert_SMILES_to_Image(smiles)
	display()

