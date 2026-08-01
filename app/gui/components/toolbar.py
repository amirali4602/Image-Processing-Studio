from PySide6.QtCore import Qt
from PySide6.QtWidgets import  QToolBar
from PySide6.QtGui import QAction


class MainToolbar(QToolBar):

    def __init__(self):
        super().__init__("Main Toolbar")

        self.setMovable(False)

        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.open_action = QAction("Open", self)
        self.save_action = QAction("Save", self)
        self.reset_action = QAction("Reset", self)
        self.fit_action = QAction("Fit", self)

        self.addAction(self.open_action)
        self.addAction(self.save_action)

        self.addSeparator()

        self.addAction(self.reset_action)

        self.addSeparator()

        self.addAction(self.fit_action)