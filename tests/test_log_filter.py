import cv2

from app.filters.high_pass.log_filter import LoGFilter


def test_log_filter():

    image = cv2.imread(
        "tests/assets/test.png"
    )


    result = LoGFilter().apply(
        image
    )


    assert result.shape == image.shape