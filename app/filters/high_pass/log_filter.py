import cv2
import numpy as np

from app.filters.base_filter import BaseFilter
from app.filters.filter_parameters import FilterParameter


class LoGFilter(BaseFilter):

    name = "LoG Filter"


    def __init__(
        self,
        gaussian_kernel_size: int = 5,
        sigma: float = 1.0,
        laplacian_kernel_size: int = 3
    ):

        self.gaussian_kernel_size = gaussian_kernel_size

        self.sigma = sigma

        self.laplacian_kernel_size = laplacian_kernel_size


    def apply(
        self,
        image: np.ndarray
    ) -> np.ndarray:


        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )


        blurred = cv2.GaussianBlur(
            gray,
            (
                self.gaussian_kernel_size,
                self.gaussian_kernel_size
            ),
            self.sigma
        )


        log = cv2.Laplacian(
            blurred,
            cv2.CV_64F,
            ksize=self.laplacian_kernel_size
        )


        log = np.absolute(
            log
        )


        log = np.uint8(
            np.clip(
                log,
                0,
                255
            )
        )


        return cv2.cvtColor(
            log,
            cv2.COLOR_GRAY2BGR
        )

    def parameters(self):

        return [

            FilterParameter(
                name="gaussian_kernel_size",
                value=self.gaussian_kernel_size,
                parameter_type="int",
                minimum=3,
                maximum=31,
                step=2
            ),


            FilterParameter(
                name="sigma",
                value=self.sigma,
                parameter_type="float",
                minimum=0.1,
                maximum=10,
                step=0.1
            ),


            FilterParameter(
                name="laplacian_kernel_size",
                value=self.laplacian_kernel_size,
                parameter_type="int",
                minimum=1,
                maximum=31,
                step=2
            )

        ]