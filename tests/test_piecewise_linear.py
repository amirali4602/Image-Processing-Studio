import cv2

from app.filters.intensity.piecewise_linear import (
    PiecewiseLinearTransform
)


def test_piecewise_linear():

    image = cv2.imread(
        "tests/assets/test.png"
    )


    result = PiecewiseLinearTransform().apply(
        image
    )


    assert result.shape == image.shape