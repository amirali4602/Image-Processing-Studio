from PySide6.QtWidgets import (
    QPushButton,
    QWidget,
    QVBoxLayout,
    QLabel,
    QSpinBox,
    QDoubleSpinBox,
    QComboBox,
    QFileDialog
)

from app.filters.filter_parameters import FilterParameter


class FilterParameterWidget(QWidget):

    def __init__(self):

        super().__init__()

        self.selected_image = None

        self.layout = QVBoxLayout(self)

        self.widgets = {}


    def clear(self):

        while self.layout.count():

            item = self.layout.takeAt(0)

            if item.widget():

                item.widget().deleteLater()


        self.widgets.clear()


    def load_parameters(
        self,
        parameters: list[FilterParameter]
    ):

        self.clear()


        for parameter in parameters:

            label = QLabel(
                parameter.name
            )

            self.layout.addWidget(
                label
            )


            widget = self._create_widget(
                parameter
            )


            self.widgets[
                parameter.name
            ] = widget


            self.layout.addWidget(
                widget
            )


    def _create_widget(
        self,
        parameter
    ):

        if parameter.parameter_type == "int":

            widget = QSpinBox()

            widget.setRange(
                parameter.minimum,
                parameter.maximum
            )

            widget.setSingleStep(
                parameter.step
            )


        elif parameter.parameter_type == "float":

            widget = QDoubleSpinBox()

            widget.setRange(
                parameter.minimum,
                parameter.maximum
            )

            widget.setSingleStep(
                parameter.step
            )

            widget.setDecimals(
                2
            )


        elif parameter.parameter_type == "choice":

            widget = QComboBox()

            widget.addItems(
                parameter.options
            )

        elif parameter.parameter_type == "image":

            widget = QPushButton(
                "Select Image"
            )


            widget.clicked.connect(
                lambda: self._select_image(widget)
            )

        else:

            raise ValueError(
                f"Unknown parameter type {parameter.parameter_type}"
            )


        widget.setValue(
            parameter.value
        ) if hasattr(widget, "setValue") else None


        if hasattr(widget, "setCurrentText"):

            widget.setCurrentText(
                str(parameter.value)
            )


        return widget


    def values(self):

        result = {}


        for name, widget in self.widgets.items():

            if name == "reference_image":

                result[name] = self.selected_image

                continue

            if isinstance(
                widget,
                QSpinBox
            ):

                result[name] = widget.value()


            elif isinstance(
                widget,
                QDoubleSpinBox
            ):

                result[name] = widget.value()


            elif isinstance(
                widget,
                QComboBox
            ):

                result[name] = widget.currentText()


        return result

    def _select_image(
        self,
        button
    ):

        path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Reference Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )


        if path:

            self.selected_image = path

            button.setText(
                path.split("/")[-1]
            )