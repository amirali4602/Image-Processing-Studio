from app.core.file_manager import FileManager
from app.core.image_state import ImageState


class ImageController:

    def __init__(self):

        self.state = ImageState()

    def load(self, path):

        image = FileManager.load_image(path)

        self.state.original_image = image.copy()

        self.state.current_image = image

        self.state.file_path = path

        return image

    def reset(self):

        self.state.reset()

        return self.state.current_image

    def save(self, path=None):

        if path is None:
            path = self.state.file_path

        FileManager.save_image(
            path,
            self.state.current_image,
        )