from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter
from PySide6.QtWidgets import (
    QGraphicsPixmapItem,
    QGraphicsScene,
    QGraphicsTextItem,
    QGraphicsView,
)

from app.utils.image_converter import ImageConverter


class ImageView(QGraphicsView):

    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.pixmap_item = QGraphicsPixmapItem()

        self.scene.addItem(self.pixmap_item)

        self.placeholder = QGraphicsTextItem(
            "Open an image to begin"
        )

        self.scene.addItem(self.placeholder)

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setBackgroundBrush(QColor("#202124"))

        self.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)

    def set_image(self, image):

        self.placeholder.hide()

        pixmap = ImageConverter.cv_to_pixmap(image)

        self.pixmap_item.setPixmap(pixmap)

        self.scene.setSceneRect(
            self.pixmap_item.boundingRect()
        )

        self.fit_image()

    def clear_image(self):

        self.pixmap_item.setPixmap({})

        self.placeholder.show()

    def fit_image(self):

        if self.pixmap_item.pixmap().isNull():
            return

        self.fitInView(
            self.pixmap_item,
            Qt.AspectRatioMode.KeepAspectRatio,
        )