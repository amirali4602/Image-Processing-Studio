from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QSpinBox,
    QDoubleSpinBox,
)


class Sidebar(QWidget):

    filter_selected = Signal(str)
    apply_requested = Signal(str, dict)


    def __init__(self):

        super().__init__()

        self.selected_filter = None

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
                "Gaussian Filter"
            ]
        )


        self.filter_list.currentTextChanged.connect(
            self._filter_changed
        )


        layout.addWidget(
            self.filter_list
        )


        self.kernel_label = QLabel(
            "Kernel Size"
        )

        layout.addWidget(
            self.kernel_label
        )


        self.kernel_size = QSpinBox()

        self.kernel_size.setRange(
            3,
            31
        )

        self.kernel_size.setSingleStep(
            2
        )

        self.kernel_size.setValue(
            5
        )


        layout.addWidget(
            self.kernel_size
        )


        self.sigma_label = QLabel(
            "Sigma"
        )

        layout.addWidget(
            self.sigma_label
        )


        self.sigma = QDoubleSpinBox()

        self.sigma.setRange(
            0.1,
            10
        )

        self.sigma.setValue(
            1.0
        )


        layout.addWidget(
            self.sigma
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


    def _filter_changed(self, name):

        self.selected_filter = name

        self.filter_selected.emit(
            name
        )


    def _apply(self):

        if self.selected_filter is None:
            return


        params = {
            "kernel_size":
                self.kernel_size.value(),

            "sigma":
                self.sigma.value()
        }


        self.apply_requested.emit(
            self.selected_filter,
            params
        )