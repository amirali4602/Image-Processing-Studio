import cv2

from app.filters.low_pass.box_filter import BoxFilter
from app.filters.low_pass.gaussian_filter import GaussianFilter



def test_box_filter():

    image = cv2.imread(
        "tests/assets/test.png"
    )

    result = BoxFilter().apply(image)

    assert result.shape == image.shape



def test_gaussian_filter():

    image = cv2.imread(
        "tests/assets/test.png"
    )

    result = GaussianFilter().apply(image)

    assert result.shape == image.shape