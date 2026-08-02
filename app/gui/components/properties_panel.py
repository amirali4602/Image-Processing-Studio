from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QGroupBox,
    QFormLayout,
    QListWidget
)
from app.gui.components.histogram_widget import HistogramWidget

class PropertiesPanel(QWidget):

    def __init__(self):

        super().__init__()

        self.histogram = HistogramWidget()
        self.history_list = QListWidget()
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

        # Statistics Section

        statistics_group = QGroupBox(
            "Image Statistics"
        )


        statistics_form = QFormLayout()


        self.minimum_label = QLabel("-")

        self.maximum_label = QLabel("-")

        self.mean_label = QLabel("-")

        self.std_label = QLabel("-")


        statistics_form.addRow(
            "Minimum:",
            self.minimum_label
        )


        statistics_form.addRow(
            "Maximum:",
            self.maximum_label
        )


        statistics_form.addRow(
            "Mean:",
            self.mean_label
        )


        statistics_form.addRow(
            "Standard Deviation:",
            self.std_label
        )


        statistics_group.setLayout(
            statistics_form
        )


        layout.addWidget(
            statistics_group
        )

        histogram_group = QGroupBox(
            "Histogram"
        )


        histogram_layout = QVBoxLayout()


        histogram_layout.addWidget(
            self.histogram
        )


        histogram_group.setLayout(
            histogram_layout
        )


        layout.addWidget(
            histogram_group
        )

        history_group = QGroupBox(
            "Processing History"
        )


        history_layout = QVBoxLayout()


        history_layout.addWidget(
            self.history_list
        )


        history_group.setLayout(
            history_layout
        )


        layout.addWidget(
            history_group
        )

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


    def update_statistics(
        self,
        image
    ):

        if image is None:
            return


        from app.core.image_statistics import (
            ImageStatistics
        )


        statistics = ImageStatistics(
            image
        )


        self.minimum_label.setText(
            str(statistics.minimum)
        )


        self.maximum_label.setText(
            str(statistics.maximum)
        )


        self.mean_label.setText(
            str(statistics.mean)
        )


        self.std_label.setText(
            str(statistics.standard_deviation)
        )


    def update_histogram(
        self,
        image
    ):

        self.histogram.update_histogram(
            image
        )

    def update_history(
        self,
        history
    ):

        self.history_list.clear()


        for item in history:

            self.history_list.addItem(
                item
            )