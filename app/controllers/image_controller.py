from pathlib import Path

from app.core.file_manager import FileManager
from app.core.image_state import ImageState


class ImageController:

    def __init__(self):
        self.state = ImageState()

    def load_image(self, path: str | Path):

        path = Path(path)

        image = FileManager.load_image(path)

        self.state.original_image = image.copy()
        self.state.current_image = image
        self.state.file_path = path

        return self.state.current_image


    def save_image(self):

        if not self.state.has_image:
            raise ValueError("No image loaded.")

        if self.state.file_path is None:
            raise ValueError("Image has no file path.")

        FileManager.save_image(
            self.state.file_path,
            self.state.current_image
        )


    def save_image_as(self, path: str | Path):

        if not self.state.has_image:
            raise ValueError("No image loaded.")

        path = Path(path)

        FileManager.save_image(
            path,
            self.state.current_image
        )

        self.state.file_path = path


    def reset_image(self):

        return self.state.reset()