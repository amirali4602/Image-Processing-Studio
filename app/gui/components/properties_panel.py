from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QGroupBox,
    QFormLayout,
)


class PropertiesPanel(QWidget):

    def __init__(self):

        super().__init__()

        self._create_ui()


    def _create_ui(self):

        layout = QVBoxLayout(
            self
        )


        # Image Information Section

        image_group = QGroupBox(
            "Image Information"
        )


        form = QFormLayout()


        self.filename_label = QLabel("-")

        self.width_label = QLabel("-")

        self.height_label = QLabel("-")

        self.resolution_label = QLabel("-")

        self.channels_label = QLabel("-")

        self.color_label = QLabel("-")


        form.addRow(
            "Filename:",
            self.filename_label
        )


        form.addRow(
            "Width:",
            self.width_label
        )


        form.addRow(
            "Height:",
            self.height_label
        )


        form.addRow(
            "Resolution:",
            self.resolution_label
        )


        form.addRow(
            "Channels:",
            self.channels_label
        )


        form.addRow(
            "Color:",
            self.color_label
        )


        image_group.setLayout(
            form
        )


        layout.addWidget(
            image_group
        )


        layout.addStretch()


    def update_image_info(
        self,
        state
    ):

        self.filename_label.setText(
            state.file_name
        )


        self.width_label.setText(
            str(state.width)
        )


        self.height_label.setText(
            str(state.height)
        )


        self.resolution_label.setText(
            f"{state.width} x {state.height}"
        )


        if state.current_image is not None:

            channels = (
                1
                if len(state.current_image.shape) == 2
                else state.current_image.shape[2]
            )


            self.channels_label.setText(
                str(channels)
            )


            if channels == 1:

                self.color_label.setText(
                    "Grayscale"
                )

            else:

                self.color_label.setText(
                    "RGB"
                )

        else:

            self.channels_label.setText(
                "-"
            )

            self.color_label.setText(
                "-"
            )