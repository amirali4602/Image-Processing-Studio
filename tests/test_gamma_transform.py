import cv2

from app.filters.intensity.gamma_transform import GammaTransform


def test_gamma_transform():

    image = cv2.imread(
        "tests/assets/test.png"
    )


    result = GammaTransform(
        gamma=0.5
    ).apply(
        image
    )


    assert result.shape == image.shape