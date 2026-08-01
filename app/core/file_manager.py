from pathlib import Path

import cv2
import numpy as np


class FileManager:

    @staticmethod
    def load_image(path: str | Path) -> np.ndarray:

        image = cv2.imread(str(path), cv2.IMREAD_COLOR)

        if image is None:
            raise ValueError(f"Unable to load image: {path}")

        return image

    @staticmethod
    def save_image(path: str | Path, image: np.ndarray):

        success = cv2.imwrite(str(path), image)

        if not success:
            raise ValueError(f"Unable to save image: {path}")