# Sprint 5 — Histogram Processing

## Goal

Implement histogram-based image enhancement techniques.

This sprint adds the final major image processing operations required for the university project:

- Histogram Equalization
- Histogram Matching


---

# Objectives

- Create histogram processing architecture
- Implement histogram equalization
- Implement histogram matching
- Support grayscale and color images
- Add reference image selection for histogram matching
- Integrate histogram tools into the dynamic filter system


---

# Architecture

The filter architecture is extended:

```
ImageController

        |

        v

FilterManager

        |

        v

BaseFilter


        |

        +---------------------------+

        |                           |

        v                           v


Intensity Filters              Histogram Filters


Log Transformation             Histogram Equalization

Gamma Transformation            Histogram Matching

Piecewise Linear

```


---

# Histogram Equalization


## Concept

Histogram equalization improves image contrast by redistributing pixel intensity values.

It attempts to spread intensity values more evenly across the available range.


Example:


```
Low contrast image

Pixels concentrated around middle values


        |

        v


Histogram Equalization


        |

        v


Higher contrast image
```


---

## Algorithm


```
Input Image

     |

     v

Calculate Histogram

     |

     v

Calculate CDF
(Cumulative Distribution Function)

     |

     v

Map old intensities to new intensities

     |

     v

Enhanced Image
```


---

## Implementation


For grayscale images:


```python
cv2.equalizeHist()
```


For color images:


Direct equalization on RGB channels can create color distortion.


Therefore:


```
BGR Image

    |

    v

Convert to LAB

    |

    v

Equalize L channel

    |

    v

Convert back to BGR

    |

    v

Output Image
```


---

# Histogram Matching


## Concept

Histogram matching transforms an image so that its histogram becomes similar to a reference image.


Example:


```
Input Image


dark image histogram


        +


Reference Image


desired histogram


        |


        v


Histogram Mapping


        |


        v


Matched Image
```


---

# Algorithm


```
Input Image

        |

        v

Calculate Source Histogram

        |

        v

Calculate Source CDF



Reference Image

        |

        v

Calculate Reference Histogram

        |

        v

Calculate Reference CDF



        |

        v


Create Intensity Mapping


        |

        v


Apply Mapping


        |

        v


Output Image
```


---

# Filter Parameters


## Histogram Equalization


No parameters:


```
Histogram Equalization

        |

        v

Apply
```


---

## Histogram Matching


Parameters:


```
Reference Image

[ Select Image ]

```


---

# UI Changes


Filter list becomes:


```
Filters


Low Pass

    Box Filter

    Gaussian Filter



High Pass

    Sobel Filter

    Laplacian Filter

    LoG Filter



Intensity

    Log Transformation

    Power Law (Gamma)

    Piecewise Linear



Histogram

    Histogram Equalization

    Histogram Matching
```


---

# Processing Flow


## Histogram Equalization


```
User selects Histogram Equalization


        |

        v


Apply Button


        |

        v


HistogramEqualizationFilter


        |

        v


Update ImageView
```


---

## Histogram Matching


```
User selects Histogram Matching


        |

        v


Select Reference Image


        |

        v


Apply


        |

        v


HistogramMatchingFilter


        |

        v


Update ImageView
```


---

# Testing


Test with:


- Low contrast images
- Bright images
- Dark images
- Color images
- Different reference images


Expected:


Histogram Equalization:

- Improved contrast
- Better intensity distribution


Histogram Matching:

- Output histogram resembles reference histogram


---

# Sprint Deliverables


At the end of Sprint 5:


The application supports:


## Filtering

- Box Filter
- Gaussian Filter
- Sobel Filter
- Laplacian Filter
- LoG Filter


## Intensity Transformations

- Log Transformation
- Power Law (Gamma)
- Piecewise Linear Transformation


## Histogram Processing

- Histogram Equalization
- Histogram Matching


---

# Git Commits


Recommended:


```bash
feat(histogram): add histogram filter architecture

feat(histogram): implement histogram equalization

feat(histogram): implement histogram matching

feat(ui): add histogram filter controls
```


---

# Next Sprint


Sprint 6 will focus on:

- Image analysis tools
- Histogram visualization
- Image statistics
- Processing history
- Undo/Redo system