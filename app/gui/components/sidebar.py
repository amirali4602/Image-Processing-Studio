from PySide6.QtWidgets import (
    QTreeWidget,
    QTreeWidgetItem,
)


class Sidebar(QTreeWidget):

    def __init__(self):
        super().__init__()

        self.setHeaderHidden(True)

        self._build_tree()

    def _build_tree(self):

        low = QTreeWidgetItem(["Low Pass"])
        low.addChild(QTreeWidgetItem(["Box Filter"]))
        low.addChild(QTreeWidgetItem(["Gaussian Filter"]))

        high = QTreeWidgetItem(["High Pass"])
        high.addChild(QTreeWidgetItem(["Sobel"]))
        high.addChild(QTreeWidgetItem(["LoG"]))

        intensity = QTreeWidgetItem(["Intensity"])
        intensity.addChild(QTreeWidgetItem(["Log"]))
        intensity.addChild(QTreeWidgetItem(["Gamma"]))
        intensity.addChild(QTreeWidgetItem(["Piecewise"]))

        histogram = QTreeWidgetItem(["Histogram"])
        histogram.addChild(QTreeWidgetItem(["Equalization"]))
        histogram.addChild(QTreeWidgetItem(["Matching"]))

        self.addTopLevelItem(low)
        self.addTopLevelItem(high)
        self.addTopLevelItem(intensity)
        self.addTopLevelItem(histogram)

        self.expandAll()