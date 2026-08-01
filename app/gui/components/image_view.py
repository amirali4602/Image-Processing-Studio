from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter, QPixmap
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
        self._zoom = 0

        self._zoom_step = 1.15

        self._empty = True
        

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.pixmap_item = QGraphicsPixmapItem()

        self.scene.addItem(self.pixmap_item)

        self.placeholder = QGraphicsTextItem(
            "Open an image to begin"
        )

        self.scene.addItem(self.placeholder)

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setBackgroundBrush(QColor("#2b2b2b"))

        self.setRenderHints(
            QPainter.RenderHint.Antialiasing
            | QPainter.RenderHint.SmoothPixmapTransform
        )

        self.setDragMode(
            QGraphicsView.DragMode.ScrollHandDrag
        )

    def set_image(self, image):

        self.placeholder.hide()

        pixmap = ImageConverter.cv_to_pixmap(image)

        self.pixmap_item.setPixmap(pixmap)

        self.scene.setSceneRect(
            self.pixmap_item.boundingRect()
        )

        self._empty = False
        self._zoom = 0

        self.fit_image()

    def clear_image(self):

        self.pixmap_item.setPixmap(QPixmap())

        self.placeholder.show()

        self._empty = True
        self._zoom = 0

    def fit_image(self):

        if self._empty:
            return

        self.fitInView(
            self.pixmap_item,
            Qt.AspectRatioMode.KeepAspectRatio
        )

        self._zoom = 0

    def wheelEvent(self, event):

        if self._empty:
            return

        if event.angleDelta().y() > 0:

            factor = self._zoom_step

            self._zoom += 1

        else:

            factor = 1 / self._zoom_step

            self._zoom -= 1

        self.scale(factor, factor)
    def mouseDoubleClickEvent(self, event):

        self.fit_image()

        super().mouseDoubleClickEvent(event)