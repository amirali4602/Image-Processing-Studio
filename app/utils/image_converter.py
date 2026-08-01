import cv2

from PySide6.QtGui import (
    QImage,
    QPixmap,
)


class ImageConverter:

    @staticmethod
    def cv_to_pixmap(image):

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        h, w, ch = rgb.shape

        bytes_per_line = ch * w

        qimage = QImage(
            rgb.data,
            w,
            h,
            bytes_per_line,
            QImage.Format.Format_RGB888,
        )

        return QPixmap.fromImage(qimage.copy())