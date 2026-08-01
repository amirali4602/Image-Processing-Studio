# Sprint 3 — High-Pass Filters & Edge Detection


## Goal

Implement high-pass filtering techniques for detecting edges and image details.

This sprint extends the existing filter framework with edge detection algorithms.

---

# Objectives

- Create high-pass filter architecture
- Implement Sobel filters
- Implement Laplacian filter
- Implement Laplacian of Gaussian (LoG)
- Add edge detection parameters
- Integrate filters into the UI


---

# Architecture

The existing filter architecture is extended:


```
ImageController

        |

        v

FilterManager

        |

        v

BaseFilter


        |

        +----------------------+

        |                      |

        v                      v


Low Pass              High Pass


BoxFilter             SobelFilter

GaussianFilter        LaplacianFilter

                       LoGFilter

```


---

# High-Pass Filters


## Concept

High-pass filters emphasize rapid intensity changes.

They are used for:

- Edge detection
- Feature extraction
- Image sharpening


Example:


```
Smooth Region

100 100 100
100 100 100
100 100 100



Edge Region

100 100 100
100 200 200
100 200 200

```


---

# Implemented Filters


## Sobel Filter


### Description

Detects image gradients in horizontal and vertical directions.


Uses:

```python
cv2.Sobel()
```


Modes:


```
Sobel X

Detect vertical edges



Sobel Y

Detect horizontal edges



Magnitude

Combine X and Y gradients
```



Parameters:

- Kernel size


---


## Laplacian Filter


### Description

Detects areas of rapid intensity change using second derivatives.


Uses:


```python
cv2.Laplacian()
```


Parameters:

- Kernel size


---


## Laplacian of Gaussian (LoG)


### Description

A combination of:

1. Gaussian smoothing
2. Laplacian edge detection


Pipeline:


```
Input Image

     |

Gaussian Blur

     |

Laplacian

     |

Edge Image

```



Parameters:

- Gaussian kernel size
- Sigma
- Laplacian kernel size


---

# UI Changes


Filter list:


```
Filters


Low Pass

    Box Filter
    Gaussian Filter


High Pass

    Sobel X
    Sobel Y
    Sobel Magnitude
    Laplacian
    LoG

```


Dynamic parameters:


Example:

```
Sobel Filter


Kernel Size:

[ 3 ]


Apply

```


---

# Processing Flow


```
User selects Sobel


        |


Properties Panel


        |


Apply


        |


ImageController


        |


FilterManager


        |


SobelFilter


        |


Update ImageView

```


---

# Testing


Filters should be tested with:


- Grayscale images
- RGB images
- Different kernel sizes
- Images with strong edges


Expected:


- Edges become visible
- Flat regions become darker


---

# Sprint Deliverables


At the end of Sprint 3:


The application supports:


- Box Filter
- Gaussian Filter
- Sobel X
- Sobel Y
- Sobel Magnitude
- Laplacian
- LoG



---

# Git Commits


Recommended:


```bash
feat(filters): add high pass filter architecture

feat(filters): implement sobel filters

feat(filters): implement laplacian filters

feat(filters): implement log filter

feat(ui): add high pass filter controls
```


---

# Next Sprint


Sprint 4 will implement:

- Power-law transformation
- Log transformation
- Piecewise linear transformation