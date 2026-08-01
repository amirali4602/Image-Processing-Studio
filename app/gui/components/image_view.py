from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsTextItem,
    QGraphicsView,
)


class ImageView(QGraphicsView):

    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.setAlignment(Qt.AlignCenter)

        self.setRenderHints(
            self.renderHints()
        )

        self.setDragMode(QGraphicsView.NoDrag)

        self.setBackgroundBrush(QColor("#202124"))

        self.setFrameShape(QGraphicsView.NoFrame)

        text = QGraphicsTextItem("Open an image to begin")

        font = QFont()
        font.setPointSize(16)

        text.setFont(font)
        text.setDefaultTextColor(QColor("#9AA0A6"))

        self.scene.addItem(text)

        text.setPos(-70, -10)