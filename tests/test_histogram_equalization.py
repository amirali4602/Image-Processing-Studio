import cv2

from app.filters.histogram.histogram_equalization import (
    HistogramEqualization
)


def test_histogram_equalization():

    image = cv2.imread(
        "tests/assets/test.png"
    )


    result = HistogramEqualization().apply(
        image
    )


    assert result.shape == image.shape