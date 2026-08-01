from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QWidget,
    QMessageBox,
    QLabel,
    QDockWidget,
    QFileDialog
)
from app.controllers.image_controller import ImageController
from app.gui.components.image_view import ImageView
from app.gui.components.properties_panel import PropertiesPanel
from app.gui.components.sidebar import Sidebar
from app.gui.components.toolbar import MainToolbar
from PySide6.QtGui import QIcon
from app.gui.styles import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image_controller = ImageController()

        self._configure_window()

        self._create_menu()
        self._create_toolbar()
        self._connect_actions()
        self._create_statusbar()
        self._create_ui()

    def _configure_window(self):

        self.setWindowTitle(WINDOW_TITLE)
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setMinimumSize(MIN_WIDTH, MIN_HEIGHT)

    def _connect_actions(self):

        self.toolbar.open_action.triggered.connect(
            self.open_image
        )

        self.open_action.triggered.connect(
            self.open_image
        )

    def open_image(self):

        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp *.tif)"
        )

        if not path:
            return

        self.image_controller.load_image(path)

        self.image_view.set_image(
            self.image_controller.state.current_image
        )

        self.status_label.setText(
            f"Loaded {self.image_controller.state.file_name}"
        )

        self.image_info_label.setText(
            f"{self.image_controller.state.width} × {self.image_controller.state.height}"
        )

    def _create_menu(self):

        file_menu = self.menuBar().addMenu("&File")

        self.open_action = file_menu.addAction("Open")
        self.save_action = file_menu.addAction("Save")

        file_menu.addSeparator()

        self.exit_action = file_menu.addAction("Exit")
        self.exit_action.triggered.connect(self.close)
        self.open_action.setShortcut("Ctrl+O")
        self.save_action.setShortcut("Ctrl+S")
        self.exit_action.setShortcut("Ctrl+Q")
        self.menuBar().addMenu("&View")
        help_menu = self.menuBar().addMenu("&Help")

        self.about_action = help_menu.addAction("About")

        self.about_action.triggered.connect(self.show_about)

    def _create_toolbar(self):

        self.toolbar = MainToolbar()

        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)

    def _create_statusbar(self):

        self.status_label = QLabel("Ready")

        self.image_info_label = QLabel("No image loaded")

        self.statusBar().addWidget(self.status_label)

        self.statusBar().addPermanentWidget(self.image_info_label)

    def _create_ui(self):

        central = QWidget()

        self.setCentralWidget(central)

        layout = QHBoxLayout(central)
        layout.setContentsMargins(10, 10, 10, 10)

        layout.setSpacing(10)
        self.sidebar = Sidebar()
        self.sidebar.setFixedWidth(250)

        self.image_view = ImageView()

        self.properties = PropertiesPanel()
        self.properties.setFixedWidth(280)

        self.setCentralWidget(self.image_view)
        self.sidebar_dock = QDockWidget("Filters", self)

        self.sidebar_dock.setWidget(self.sidebar)

        self.addDockWidget(
            Qt.LeftDockWidgetArea,
            self.sidebar_dock
        )

        self.properties_dock = QDockWidget(
            "Properties",
            self
        )

        self.properties_dock.setWidget(
            self.properties
        )

        self.addDockWidget(
            Qt.RightDockWidgetArea,
            self.properties_dock
        )
        self.sidebar.setFixedWidth(SIDEBAR_WIDTH)

    def show_about(self):
        QMessageBox.about(
            self,
            "About",
            """
            <h2>Image Processing Studio</h2>

            <p>Version 1.0</p>

            <p>Built with:</p>

            <ul>
            <li>Python</li>
            <li>PySide6</li>
            <li>OpenCV</li>
            <li>NumPy</li>
            </ul>
            """
        )