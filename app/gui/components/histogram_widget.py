import matplotlib

matplotlib.use("QtAgg")


from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg
)

from matplotlib.figure import Figure

from PySide6.QtWidgets import QWidget, QVBoxLayout

import cv2
import numpy as np



class HistogramWidget(QWidget):

    def __init__(self):

        super().__init__()


        self.figure = Figure(
            figsize=(5, 3)
        )


        self.canvas = (
            FigureCanvasQTAgg(
                self.figure
            )
        )


        layout = QVBoxLayout(
            self
        )


        layout.addWidget(
            self.canvas
        )


    def update_histogram(
        self,
        image
    ):

        if image is None:
            return


        self.figure.clear()


        axis = self.figure.add_subplot(
            111
        )


        if len(image.shape) == 2:

            axis.hist(
                image.ravel(),
                bins=256,
                range=(0,255)
            )


        else:

            colors = (
                "b",
                "g",
                "r"
            )


            for index, color in enumerate(colors):

                histogram = cv2.calcHist(
                    [image],
                    [index],
                    None,
                    [256],
                    [0,256]
                )


                axis.plot(
                    histogram,
                    color=color
                )


        axis.set_xlim(
            0,
            255
        )


        axis.set_title(
            "Histogram"
        )


        axis.set_xlabel(
            "Intensity"
        )


        axis.set_ylabel(
            "Pixels"
        )


        self.canvas.draw()