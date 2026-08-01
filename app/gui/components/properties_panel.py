from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)


class PropertiesPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Properties")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title)

        self.content = QLabel(
            "Select a filter from the sidebar."
        )

        self.content.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.content)

        layout.addStretch()