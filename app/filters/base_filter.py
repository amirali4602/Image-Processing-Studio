from abc import ABC, abstractmethod

import numpy as np


class BaseFilter(ABC):
    """
    Base class for all image processing filters.
    """

    name: str = "Base Filter"


    @abstractmethod
    def apply(
        self,
        image: np.ndarray
    ) -> np.ndarray:
        """
        Process an image and return the result.
        """

        pass