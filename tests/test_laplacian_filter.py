import cv2

from app.filters.high_pass.laplacian_filter import LaplacianFilter


def test_laplacian_filter():

    image = cv2.imread(
        "tests/assets/test.png"
    )


    result = LaplacianFilter().apply(
        image
    )


    assert result.shape == image.shape