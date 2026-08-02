# Image Processing Studio

A desktop image processing application built with Python, PySide6, OpenCV, and NumPy.

The application provides a graphical interface for loading images, applying different image processing techniques, visualizing results, and analyzing image properties.

---

## Features

### Image Management

- Open image files
- Save processed images
- Save images with a new filename
- Reset image to its original state
- Drag and drop image loading

Supported formats:

- PNG
- JPG / JPEG
- BMP

---

# Image Processing Filters

## Low-Pass Filters

### Box Filter

Applies average filtering for noise reduction and image smoothing.

Parameters:

- Kernel size


### Gaussian Filter

Uses Gaussian convolution for image smoothing while preserving more image details.

Parameters:

- Kernel size
- Sigma value


---

## High-Pass Filters

### Sobel Filter

Detects edges using gradient calculations in horizontal and vertical directions.


### Laplacian Filter

Detects edges by measuring second-order image intensity changes.


### Laplacian of Gaussian (LoG)

Combines Gaussian smoothing with Laplacian edge detection.

Parameters:

- Kernel size
- Sigma value

---

# Intensity Transformations

## Log Transformation

Enhances details in darker regions of an image.


## Power-Law (Gamma) Transformation

Adjusts image brightness and contrast using gamma correction.

Parameters:

- Gamma value


## Piecewise Linear Transformation

Applies custom intensity mapping using linear segments.

---

# Histogram Processing

## Histogram Equalization

Improves image contrast by redistributing pixel intensity values.


## Histogram Matching

Adjusts an image histogram to match the distribution of a reference image.

Features:

- Reference image selection
- Histogram-based intensity transformation

---

# Image Analysis

The application provides an image properties panel containing:

## Image Information

Displays:

- Filename
- Image dimensions
- Resolution
- Number of channels
- Color format


## Image Statistics

Calculates:

- Minimum intensity
- Maximum intensity
- Mean intensity
- Standard deviation


## Histogram Visualization

Displays:

- Grayscale histograms
- RGB channel histograms


## Processing History

Tracks applied operations:

Example:

```
Original Image

↓

Gaussian Filter

↓

Sobel Filter

↓

Histogram Equalization
```

---

# User Interface

The application is built using PySide6 and provides:

- Toolbar controls
- Filter sidebar
- Image viewer
- Properties analysis panel
- Status bar information


Layout:

```
+------------------------------------------------+

| Toolbar                                        |

+----------+----------------------+--------------+

| Filters  |    Image Viewer      | Properties   |

|          |                      |              |

|          |                      | Information  |

|          |                      | Statistics   |

|          |                      | Histogram    |

|          |                      | History      |

+----------+----------------------+--------------+

| Status Bar                                     |

+------------------------------------------------+
```

---

# Technologies Used

## Programming Language

- Python


## GUI Framework

- PySide6


## Image Processing

- OpenCV
- NumPy


## Visualization

- Matplotlib


---

# Project Structure

```
Image Processing Studio
│
├── app
│   │
│   ├── core
│   │   ├── file_manager.py
│   │   ├── image_state.py
│   │   ├── image_statistics.py
│   │   └── history_manager.py
│   │
│   ├── controllers
│   │   └── image_controller.py
│   │
│   ├── filters
│   │   ├── filter_manager.py
│   │   ├── filter_registry.py
│   │   └── filters
│   │
│   ├── gui
│   │   ├── main_window.py
│   │   ├── components
│   │   └── styles
│   │
│   └── resources
│
├── docs
│
├── main.py
│
└── requirements.txt
```

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project folder:

```bash
cd Image-Processing-Studio
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Application

Start the application:

```bash
python main.py
```

---

# Academic Project

This project was developed as a university Image Processing final project.

It demonstrates practical implementation of:

- Spatial filtering
- Edge detection
- Intensity transformations
- Histogram processing
- Image analysis techniques

---

# License

This project is available for educational and personal use.