# Architecture

The application follows a layered architecture.

GUI
↓
Controllers
↓
Image State
↓
Filters
↓
OpenCV / NumPy

## Components

### GUI

Contains all Qt widgets.

- MainWindow
- Sidebar
- Toolbar
- PropertiesPanel
- ImageView

### Controllers

Coordinates the interaction between the GUI and the processing layer.

### Filters

Each image-processing algorithm is implemented as an independent module.

### Core

Stores application state and shared models.

### Utils

Helper functions and conversions.