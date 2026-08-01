import numpy as np

from app.filters.base_filter import BaseFilter


class TestFilter(BaseFilter):

    name = "Test Filter"


    def apply(
        self,
        image: np.ndarray
    ) -> np.ndarray:

        return image