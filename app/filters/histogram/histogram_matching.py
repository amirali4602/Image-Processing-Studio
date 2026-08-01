import cv2
import numpy as np

from app.filters.base_filter import BaseFilter
from app.filters.filter_parameters import FilterParameter


class HistogramMatching(BaseFilter):

    name = "Histogram Matching"


    def __init__(
        self,
        reference_image=None
    ):

        self.reference_image = reference_image


    def parameters(self):

        return [

            FilterParameter(
                name="reference_image",
                value=self.reference_image,
                parameter_type="image"
            )

        ]


    def apply(
        self,
        image: np.ndarray
    ) -> np.ndarray:


        if self.reference_image is None:

            raise ValueError(
                "Reference image is required"
            )


        if isinstance(
            self.reference_image,
            str
        ):

            self.reference_image = cv2.imread(
                self.reference_image
            )


            if self.reference_image is None:

                raise ValueError(
                    "Could not load reference image"
                )

        matched_channels = []


        for channel in range(3):

            source_channel = image[:, :, channel]

            reference_channel = (
                self.reference_image[:, :, channel]
            )


            matched = self._match_channel(
                source_channel,
                reference_channel
            )


            matched_channels.append(
                matched
            )


        return cv2.merge(
            matched_channels
        )


    def _match_channel(
        self,
        source,
        reference
    ):

        source_hist = cv2.calcHist(
            [source],
            [0],
            None,
            [256],
            [0,256]
        )


        reference_hist = cv2.calcHist(
            [reference],
            [0],
            None,
            [256],
            [0,256]
        )


        source_cdf = (
            source_hist.cumsum()
        )

        reference_cdf = (
            reference_hist.cumsum()
        )


        source_cdf /= source_cdf[-1]

        reference_cdf /= reference_cdf[-1]


        mapping = np.zeros(
            256,
            dtype=np.uint8
        )


        for source_value in range(256):

            difference = np.abs(
                reference_cdf -
                source_cdf[source_value]
            )


            mapping[source_value] = (
                np.argmin(difference)
            )


        return mapping[source]