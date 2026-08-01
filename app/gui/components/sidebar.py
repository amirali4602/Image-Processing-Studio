from PySide6.QtWidgets import (
    QGroupBox,
    QLabel,
    QVBoxLayout,
    QWidget,
)


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        sections = [
            "Low Pass",
            "High Pass",
            "Intensity",
            "Histogram",
        ]

        for section in sections:
            group = QGroupBox(section)

            inner = QVBoxLayout()
            inner.addWidget(QLabel("Coming in next sprints"))

            group.setLayout(inner)

            layout.addWidget(group)

        layout.addStretch()