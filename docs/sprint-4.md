# Sprint 4 — Intensity Transformations


## Goal

Implement intensity transformation techniques used for image enhancement.


## Filters


### Log Transformation

Purpose:

- Expand dark pixel values
- Improve visibility in dark regions


Formula:

s = c log(1+r)


Implementation:

OpenCV + NumPy


---


### Power-Law (Gamma) Transformation

Purpose:

Control brightness.


Formula:

s = c(r^gamma)


Parameters:

- Gamma value


Examples:

gamma < 1

Brighten image


gamma > 1

Darken image



---


### Piecewise Linear Transformation

Purpose:

Modify contrast using multiple intensity ranges.


Parameters:

- r1
- r2
- s1
- s2


Used for:

- Contrast stretching
- Threshold enhancement


---


## UI


Dynamic parameters:


Gamma:
 gamma


Piecewise:
r1
s1
r2
s2



---


## Deliverables


Application supports:


✅ Low-pass filters

✅ High-pass filters

⬜ Log transformation

⬜ Gamma transformation

⬜ Piecewise linear transformation