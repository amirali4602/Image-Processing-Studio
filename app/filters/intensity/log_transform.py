import cv2
import numpy as np

from app.filters.base_filter import BaseFilter
from app.filters.filter_parameters import FilterParameter


class LogTransform(BaseFilter):

    name = "Log Transformation"


    def __init__(
        self,
        constant: float = 1.0
    ):

        self.constant = constant


    def parameters(self):

        return [

            FilterParameter(
                name="constant",
                value=self.constant,
                parameter_type="float",
                minimum=0.1,
                maximum=10.0,
                step=0.1
            )

        ]


    def apply(
        self,
        image: np.ndarray
    ) -> np.ndarray:


        image_float = (
            image.astype(
                np.float32
            )
        )


        transformed = (
            self.constant *
            np.log(
                1 + image_float
            )
        )


        transformed = (
            transformed /
            transformed.max()
            *
            255
        )


        transformed = np.uint8(
            transformed
        )


        return transformed