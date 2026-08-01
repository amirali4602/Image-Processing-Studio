import numpy as np


class ImageStatistics:

    def __init__(
        self,
        image: np.ndarray
    ):

        self.image = image


    @property
    def minimum(self):

        return int(
            np.min(
                self.image
            )
        )


    @property
    def maximum(self):

        return int(
            np.max(
                self.image
            )
        )


    @property
    def mean(self):

        return round(
            float(
                np.mean(
                    self.image
                )
            ),
            2
        )


    @property
    def standard_deviation(self):

        return round(
            float(
                np.std(
                    self.image
                )
            ),
            2
        )


    def as_dict(self):

        return {
            "minimum": self.minimum,
            "maximum": self.maximum,
            "mean": self.mean,
            "standard_deviation": self.standard_deviation
        }