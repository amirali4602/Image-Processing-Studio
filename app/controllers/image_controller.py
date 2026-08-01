from pathlib import Path

from app.core.file_manager import FileManager
from app.core.image_state import ImageState
from app.filters.filter_manager import FilterManager
from app.filters.filter_registry import register_filters

class ImageController:

    def __init__(self):
        self.state = ImageState()
        self.filter_manager = FilterManager()
        register_filters(
            self.filter_manager
        )

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

    def apply_filter(
        self,
        filter_name,
        params
    ):

        result = self.preview_filter(
            filter_name,
            params
        )


        self.state.current_image = result

        return result

    def preview_filter(
        self,
        filter_name,
        params
    ):

        if self.state.original_image is None:
            raise ValueError(
                "No image loaded."
            )


        image_filter = (
            self.filter_manager
            .get_filter(filter_name)
        )


        for key, value in params.items():

            if hasattr(
                image_filter,
                key
            ):

                setattr(
                    image_filter,
                    key,
                    value
                )


        result = image_filter.apply(
            self.state.original_image
        )


        self.state.preview_image = result


        return result