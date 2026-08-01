import cv2
import numpy as np

from app.filters.base_filter import BaseFilter


class SobelFilter(BaseFilter):

    name = "Sobel Filter"


    def __init__(
        self,
        direction: str = "Magnitude",
        kernel_size: int = 3
    ):

        self.direction = direction
        self.kernel_size = kernel_size


    def apply(
        self,
        image: np.ndarray
    ) -> np.ndarray:


        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )


        if self.direction == "X":

            sobel = cv2.Sobel(
                gray,
                cv2.CV_64F,
                1,
                0,
                ksize=self.kernel_size
            )


        elif self.direction == "Y":

            sobel = cv2.Sobel(
                gray,
                cv2.CV_64F,
                0,
                1,
                ksize=self.kernel_size
            )


        else:

            sobel_x = cv2.Sobel(
                gray,
                cv2.CV_64F,
                1,
                0,
                ksize=self.kernel_size
            )


            sobel_y = cv2.Sobel(
                gray,
                cv2.CV_64F,
                0,
                1,
                ksize=self.kernel_size
            )


            sobel = np.sqrt(
                sobel_x ** 2 +
                sobel_y ** 2
            )


        sobel = np.absolute(
            sobel
        )


        sobel = np.uint8(
            np.clip(
                sobel,
                0,
                255
            )
        )


        return cv2.cvtColor(
            sobel,
            cv2.COLOR_GRAY2BGR
        )