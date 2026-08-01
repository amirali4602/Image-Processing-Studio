# Sprint 2 — Filter Framework & Low-Pass Filters

## Goal

Build the foundation for the image processing pipeline and implement the first image processing algorithms.

This sprint introduces a modular filter architecture that allows future filters such as Sobel, LoG, Gamma, Histogram Equalization, and Histogram Matching to be added easily.

---

# Objectives

- Create a reusable filter framework
- Separate processing algorithms from GUI code
- Implement filter management
- Implement low-pass filters
- Connect filters with ImageController
- Add basic filter execution workflow

---

# Architecture

The image processing pipeline:

```
User Interface

      |
      v

ImageController

      |
      v

FilterManager

      |
      v

BaseFilter

      |
      +----------------+
      |                |
      v                v

 BoxFilter       GaussianFilter

      |
      v

Processed Image

      |
      v

ImageView
```

---

# New Folder Structure

```
app/

├── filters/
│
│   ├── __init__.py
│   │
│   ├── base_filter.py
│   │
│   ├── filter_manager.py
│   │
│   └── low_pass/
│       │
│       ├── __init__.py
│       ├── box_filter.py
│       └── gaussian_filter.py
│
├── controllers/
│
│   └── image_controller.py
│
└── gui/
```

---

# Filter System

All filters inherit from the same base class.

Example:

```python
class BaseFilter:

    def apply(self, image):
        raise NotImplementedError
```

Every filter receives:

```
Input Image

      |

Processing

      |

Output Image
```

---

# Implemented Filters

## Box Filter

### Description

A low-pass averaging filter.

Each pixel is replaced by the average value of neighboring pixels.

Uses:

```python
cv2.blur()
```

Parameters:

- Kernel size

Examples:

```
3x3
5x5
7x7
```

---

## Gaussian Filter

### Description

A weighted smoothing filter based on the Gaussian function.

Used for:

- Noise reduction
- Image smoothing
- Preprocessing before edge detection

Uses:

```python
cv2.GaussianBlur()
```

Parameters:

- Kernel size
- Sigma value

---

# Controller Integration

ImageController will expose:

```python
apply_filter(filter)
```

Workflow:

```
Current Image

      |

Selected Filter

      |

Processed Image

      |

Update ImageState

      |

Refresh ImageView
```

---

# GUI Integration

The Properties Panel will later support:

```
Filter:

Gaussian Filter


Kernel Size:

[ 5 ]


Sigma:

[ 1.5 ]


[ Apply ]
```

---

# Testing

Filters should be tested with:

- Different image sizes
- RGB images
- Grayscale images
- Different kernel sizes

---

# Sprint Deliverables

At the end of Sprint 2:

The application can:

- Load an image
- Select a filter
- Apply a low-pass filter
- Display the result
- Reset the image

---

# Completed Tasks

## Filter Framework

- [ ] BaseFilter
- [ ] FilterManager
- [ ] Filter registration


## Low-Pass Filters

- [ ] Box Filter
- [ ] Gaussian Filter


## Integration

- [ ] Controller support
- [ ] UI support
- [ ] Filter execution flow


---

# Git Commits

Recommended commits:

```bash
feat(filters): create filter framework

feat(filters): implement box filter

feat(filters): implement gaussian filter

feat(filters): connect filters to controller
```

---

# Next Sprint

Sprint 3 will implement high-pass filtering:

- Sobel X
- Sobel Y
- Sobel magnitude
- Laplacian of Gaussian