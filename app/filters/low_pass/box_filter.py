import cv2
import numpy as np
from app.filters.filter_parameters import FilterParameter
from app.filters.base_filter import BaseFilter


class BoxFilter(BaseFilter):

    name = "Box Filter"

    def __init__(self, kernel_size: int = 5):

        self.kernel_size = kernel_size


    def apply(
        self,
        image: np.ndarray
    ) -> np.ndarray:

        return cv2.blur(
            image,
            (
                self.kernel_size,
                self.kernel_size
            )
        )

    def parameters(self):

        return [
            FilterParameter(
                name="kernel_size",
                value=self.kernel_size,
                parameter_type="int",
                minimum=3,
                maximum=31,
                step=2
            )
        ]