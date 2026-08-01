# Sprint 6 — Properties & Image Analysis Panel


## Goal

Transform the right docked Properties panel from a placeholder into a professional image analysis dashboard.

The goal of this sprint is to provide users with information about the loaded image, its properties, statistics, histogram visualization, and processing history.


---

# Objectives

Implement:

- Image metadata display
- Image statistics calculation
- Histogram visualization
- Processing history tracking
- Improved Properties panel UI


---

# Features


## 1. Image Information Panel


Display basic image metadata:


- Filename
- File path
- Width
- Height
- Resolution
- Number of channels
- Color format
- File size


Example:

```
Image Information

Filename:
example.png

Resolution:
1920 x 1080

Channels:
3

Color:
RGB

Size:
2.4 MB
```


---

# 2. Image Statistics


Calculate and display pixel statistics.


Required values:


- Minimum intensity
- Maximum intensity
- Mean intensity
- Standard deviation


Example:

```
Image Statistics

Minimum:
0

Maximum:
255

Mean:
126.4

Standard Deviation:
52.8
```


These statistics help demonstrate the effect of image processing operations.


Example:


Before histogram equalization:

```
Mean:
80

Std:
25
```


After:

```
Mean:
130

Std:
60
```


---

# 3. Histogram Visualization


Add histogram visualization inside the Properties panel.


Support:


- Grayscale histogram
- RGB histogram


Example:

```
Histogram


Intensity

0 -------------------- 255


        █
     █  █
  █  █  █  █
-----------------------
```


Implementation:

Use:

- Matplotlib
- PySide6 embedding


---

# 4. Processing History


Track all applied operations.


Example:


```
Processing History


Original Image

↓

Gaussian Filter

↓

Sobel Filter

↓

Histogram Equalization
```


The user should be able to see the sequence of transformations applied to the image.


---

# Architecture


Current:

```
ImageController

        |

        v

ImageState

        |

        v

ImageView
```


New:

```
                    ImageController

                           |

                           v

                      ImageState

                           |

        +------------------+------------------+

        |                                     |

        v                                     v


PropertiesPanel                     HistoryManager


        |

        v


HistogramWidget

```


---

# New Components


## Image Statistics


Location:


```
app/core/image_statistics.py
```


Responsibilities:


- Analyze image arrays
- Calculate statistics
- Provide formatted information


Example:


```python
statistics = ImageStatistics(image)

statistics.mean

statistics.maximum
```


---


## History Manager


Location:


```
app/core/history_manager.py
```


Responsibilities:


- Store applied filters
- Track processing order
- Clear history on new image load


Example:


```python
history.add(
    "Gaussian Filter"
)
```


---

## Histogram Widget


Location:


```
app/gui/components/histogram_widget.py
```


Responsibilities:


- Render histogram
- Update when image changes
- Support RGB and grayscale modes


---

## Properties Panel


Location:


```
app/gui/components/properties_panel.py
```


Responsibilities:


Display:


```
Properties


Image Information


Statistics


Histogram


History
```


---

# UI Layout


Final layout:


```
+------------------------------------------------+

| Toolbar                                        |

+----------+----------------------+--------------+

|          |                      |              |

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

# Sprint Phases


## Phase 1 — Image Metadata

Implement:


- Connect PropertiesPanel with ImageState
- Show filename
- Show resolution
- Show channels
- Show image size


Status:

⬜


---


## Phase 2 — Image Statistics


Implement:


- Minimum value
- Maximum value
- Mean
- Standard deviation


Status:

⬜


---


## Phase 3 — Histogram Visualization


Implement:


- HistogramWidget
- Grayscale histogram
- RGB histogram


Status:

⬜


---


## Phase 4 — Processing History


Implement:


- HistoryManager
- Add operations after applying filters
- Display history


Status:

⬜


---


## Phase 5 — UI Polish


Improve:


- Section headers
- Icons
- Spacing
- Dark theme compatibility


Status:

⬜


---

# Testing Checklist


## Properties Panel

- [ ] Updates after opening image
- [ ] Updates after applying filters
- [ ] Clears after closing image


## Statistics

- [ ] Correct values
- [ ] Works with grayscale images
- [ ] Works with RGB images


## Histogram

- [ ] Displays correctly
- [ ] Updates after processing


## History

- [ ] Tracks operations
- [ ] Resets with new image


---

# Deliverables


At the end of Sprint 6:


The application will have:


✅ Complete filter system

✅ Complete intensity transformations

✅ Complete histogram processing

⬜ Professional image analysis panel

⬜ Histogram visualization

⬜ Processing history

⬜ Improved user experience


---

# Git Commits


Recommended:


```bash
feat(properties): add image metadata display

feat(statistics): add image statistics engine

feat(histogram): add histogram visualization

feat(history): add processing history tracking

feat(ui): polish properties panel
```


---

# Next Sprint


After Sprint 6:

Possible future improvements:

- Undo / Redo system
- Image comparison mode
- Batch processing
- Export presets
- Advanced segmentation tools
- Documentation and GitHub showcase