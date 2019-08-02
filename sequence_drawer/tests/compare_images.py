import cv2
import numpy as np


original = cv2.imread("./data/test_image.png")
duplicate = cv2.imread("./data/pictureofmolecule.png")


"""if original.shape == duplicate.shape:
	print("The images have same size and channels")
difference = cv2.subtract(original, duplicate)
b, g, r = cv2.split(difference)
if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
	print("The images are completely Equal")"""


def compare_images_task():
    if original.shape == duplicate.shape:
        print("same")
    difference = cv2.subtract(original, duplicate)
    b, g, r = cv2.split(difference)
    if (
        cv2.countNonZero(b) == 0
        and cv2.countNonZero(g) == 0
        and cv2.countNonZero(r) == 0
    ):
        print("equal")
        return 1


if __name__ == "__main__":
    compare_images_task()
