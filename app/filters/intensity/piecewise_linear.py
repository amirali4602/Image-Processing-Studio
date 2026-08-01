import numpy as np

from app.filters.base_filter import BaseFilter
from app.filters.filter_parameters import FilterParameter


class PiecewiseLinearTransform(BaseFilter):

    name = "Piecewise Linear Transformation"


    def __init__(
        self,
        r1: int = 50,
        s1: int = 0,
        r2: int = 200,
        s2: int = 255
    ):

        self.r1 = r1
        self.s1 = s1

        self.r2 = r2
        self.s2 = s2


    def parameters(self):

        return [

            FilterParameter(
                name="r1",
                value=self.r1,
                parameter_type="int",
                minimum=0,
                maximum=255,
                step=1
            ),

            FilterParameter(
                name="s1",
                value=self.s1,
                parameter_type="int",
                minimum=0,
                maximum=255,
                step=1
            ),

            FilterParameter(
                name="r2",
                value=self.r2,
                parameter_type="int",
                minimum=0,
                maximum=255,
                step=1
            ),

            FilterParameter(
                name="s2",
                value=self.s2,
                parameter_type="int",
                minimum=0,
                maximum=255,
                step=1
            )

        ]


    def apply(
        self,
        image: np.ndarray
    ) -> np.ndarray:


        result = np.zeros_like(
            image,
            dtype=np.float32
        )


        r1 = self.r1
        r2 = self.r2

        s1 = self.s1
        s2 = self.s2


        # Region 1
        mask1 = image < r1

        result[mask1] = (
            (s1 / r1)
            *
            image[mask1]
        )


        # Region 2
        mask2 = (
            (image >= r1)
            &
            (image <= r2)
        )


        result[mask2] = (
            (
                (s2 - s1)
                /
                (r2 - r1)
            )
            *
            (image[mask2] - r1)
            +
            s1
        )


        # Region 3
        mask3 = image > r2


        result[mask3] = (
            (
                (255 - s2)
                /
                (255 - r2)
            )
            *
            (image[mask3] - r2)
            +
            s2
        )


        return np.uint8(
            np.clip(
                result,
                0,
                255
            )
        )