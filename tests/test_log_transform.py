import cv2

from app.filters.intensity.log_transform import LogTransform


def test_log_transform():

    image = cv2.imread(
        "tests/assets/test.png"
    )


    result = LogTransform().apply(
        image
    )


    assert result.shape == image.shape