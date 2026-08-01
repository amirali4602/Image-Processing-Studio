from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
)

from app.gui.components.filter_parameter_widget import (
    FilterParameterWidget
)


class Sidebar(QWidget):

    apply_requested = Signal(str, dict)
    filter_changed = Signal(str)


    def __init__(self):

        super().__init__()

        self.selected_filter = None

        self.parameter_widget = FilterParameterWidget()

        self._create_ui()


    def _create_ui(self):

        layout = QVBoxLayout(self)


        title = QLabel(
            "Filters"
        )

        layout.addWidget(title)


        self.filter_list = QListWidget()

        self.filter_list.addItems(
            [
                "Box Filter",
                "Gaussian Filter",
                "Sobel Filter",
                "Laplacian Filter",
                "LoG Filter",
                "Log Transformation"
            ]
        )


        self.filter_list.currentTextChanged.connect(
            self._filter_changed
        )


        layout.addWidget(
            self.filter_list
        )


        layout.addWidget(
            self.parameter_widget
        )


        self.apply_button = QPushButton(
            "Apply"
        )


        self.apply_button.clicked.connect(
            self._apply
        )


        layout.addWidget(
            self.apply_button
        )


    def _filter_changed(
        self,
        name
    ):

        self.selected_filter = name

        self.filter_changed.emit(
            name
        )


    def _apply(self):

        if self.selected_filter is None:
            return


        params = (
            self.parameter_widget
            .values()
        )


        self.apply_requested.emit(
            self.selected_filter,
            params
        )