import cv2
import numpy as np


def compare_images_task(image_a, image_b):
    image_a = cv2.imread(str(image_a))
    image_b = cv2.imread(str(image_b))
    if image_a.shape != image_b.shape:
        return False
    difference = cv2.subtract(image_a, image_b)
    b, g, r = cv2.split(difference)
    if (
        cv2.countNonZero(b) == 0
        and cv2.countNonZero(g) == 0
        and cv2.countNonZero(r) == 0
    ):
        return True
    return False


if __name__ == "__main__":
    from pathlib import Path

    HERE = Path(__file__).parent
    original = HERE / "data/test_image.png"
    duplicate = HERE / "data/pictureofmolecule.png"
    assert compare_images_task(original, duplicate)
