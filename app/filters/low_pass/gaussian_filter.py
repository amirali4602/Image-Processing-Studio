import cv2
import numpy as np

from app.filters.base_filter import BaseFilter
from app.filters.filter_parameters import FilterParameter


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

    def parameters(self):

        return [

            FilterParameter(
                name="kernel_size",
                value=self.kernel_size,
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
            )

        ]