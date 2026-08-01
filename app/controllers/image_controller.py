from pathlib import Path

from app.core.file_manager import FileManager
from app.core.image_state import ImageState


class ImageController:

    def __init__(self):
        self.state = ImageState()

    def load_image(self, path: str | Path):
        """Load an image from disk."""

        path = Path(path)

        image = FileManager.load_image(path)

        self.state.original_image = image.copy()
        self.state.current_image = image
        self.state.file_path = path

        return image

    def save_image(self, path: str | Path | None = None):
        """Save the current image."""

        if not self.state.has_image:
            raise ValueError("No image loaded.")

        if path is None:
            path = self.state.file_path

        if path is None:
            raise ValueError("No file path specified.")

        path = Path(path)

        FileManager.save_image(path, self.state.current_image)

        self.state.file_path = path

    def reset_image(self):
        """Restore the original image."""

        return self.state.reset()