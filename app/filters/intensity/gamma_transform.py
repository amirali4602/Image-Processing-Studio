import numpy as np

from app.filters.base_filter import BaseFilter
from app.filters.filter_parameters import FilterParameter


class GammaTransform(BaseFilter):

    name = "Power Law (Gamma)"


    def __init__(
        self,
        gamma: float = 1.0,
        constant: float = 1.0
    ):

        self.gamma = gamma
        self.constant = constant


    def parameters(self):

        return [

            FilterParameter(
                name="gamma",
                value=self.gamma,
                parameter_type="float",
                minimum=0.1,
                maximum=5.0,
                step=0.1
            ),


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
            /
            255.0
        )


        transformed = (
            self.constant *
            np.power(
                image_float,
                self.gamma
            )
        )


        transformed = (
            transformed /
            transformed.max()
            *
            255
        )


        return np.uint8(
            transformed
        )