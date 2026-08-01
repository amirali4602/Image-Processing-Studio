import cv2
import numpy as np

from app.filters.base_filter import BaseFilter
from app.filters.filter_parameters import FilterParameter


class LaplacianFilter(BaseFilter):

    name = "Laplacian Filter"


    def __init__(
        self,
        kernel_size: int = 3
    ):

        self.kernel_size = kernel_size


    def apply(
        self,
        image: np.ndarray
    ) -> np.ndarray:


        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )


        laplacian = cv2.Laplacian(
            gray,
            cv2.CV_64F,
            ksize=self.kernel_size
        )


        laplacian = np.absolute(
            laplacian
        )


        laplacian = np.uint8(
            np.clip(
                laplacian,
                0,
                255
            )
        )


        return cv2.cvtColor(
            laplacian,
            cv2.COLOR_GRAY2BGR
        )

    def parameters(self):

        return [

            FilterParameter(
                name="kernel_size",
                value=self.kernel_size,
                parameter_type="int",
                minimum=1,
                maximum=31,
                step=2
            )

        ]