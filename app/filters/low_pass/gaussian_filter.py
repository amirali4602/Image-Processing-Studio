import cv2
import numpy as np

from app.filters.base_filter import BaseFilter


class GaussianFilter(BaseFilter):

    name = "Gaussian Filter"


    def __init__(
        self,
        kernel_size: int = 5,
        sigma: float = 1.0
    ):

        self.kernel_size = kernel_size
        self.sigma = sigma



    def apply(
        self,
        image: np.ndarray
    ) -> np.ndarray:


        return cv2.GaussianBlur(
            image,
            (
                self.kernel_size,
                self.kernel_size
            ),
            self.sigma
        )