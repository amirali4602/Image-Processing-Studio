from dataclasses import dataclass
from pathlib import Path

import numpy as np


@dataclass
class ImageState:
    original_image: np.ndarray | None = None
    current_image: np.ndarray | None = None

    file_path: Path | None = None

    @property
    def has_image(self) -> bool:
        return self.current_image is not None

    @property
    def width(self) -> int:
        if not self.has_image:
            return 0
        return self.current_image.shape[1]

    @property
    def height(self) -> int:
        if not self.has_image:
            return 0
        return self.current_image.shape[0]

    @property
    def file_name(self) -> str:
        if self.file_path is None:
            return "Untitled"

        return self.file_path.name

    def reset(self):
        if self.original_image is None:
            return None

        self.current_image = self.original_image.copy()
        return self.current_image