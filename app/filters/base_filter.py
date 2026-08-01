from abc import ABC, abstractmethod
from app.filters.filter_parameters import FilterParameter
import numpy as np


class BaseFilter(ABC):
    """
    Base class for all image processing filters.
    """

    name: str = "Base Filter"

    def parameters(self):

        return []
    
    @abstractmethod
    def apply(
        self,
        image: np.ndarray
    ) -> np.ndarray:
        """
        Process an image and return the result.
        """

        pass