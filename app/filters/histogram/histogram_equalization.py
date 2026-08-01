import cv2
import numpy as np

from app.filters.base_filter import BaseFilter


class HistogramEqualization(BaseFilter):

    name = "Histogram Equalization"


    def parameters(self):

        return []


    def apply(
        self,
        image: np.ndarray
    ) -> np.ndarray:


        # Convert BGR -> LAB
        lab = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2LAB
        )


        # Split channels
        l, a, b = cv2.split(
            lab
        )


        # Equalize only brightness channel
        equalized_l = cv2.equalizeHist(
            l
        )


        # Merge channels back
        result = cv2.merge(
            [
                equalized_l,
                a,
                b
            ]
        )


        # Convert LAB -> BGR
        result = cv2.cvtColor(
            result,
            cv2.COLOR_LAB2BGR
        )


        return result