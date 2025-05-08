# RGB Hexagram (Kondo 2025)
## Introduction
This software provides sample source code as a tutorial for applying the RGB (Red, Green, and Blue) hexagram, a visualization and multivariate analysis method, to 3D and higher-dimensional data.
The supported languages are now Python and fortran.  If you are a fortran user and you want to use fortran codes, please contact me with the e-mail address in [ORCID](https://orcid.org/0000-0003-4434-7877).

Please see [Kondo (2025)](https://doi.org/10.2151/sola.2025-028) for details of the visualization and multivariate analysis method.

### Licence and agreement
The source codes are distributed under the [MIT license](https://opensource.org/licenses/MIT).  
You must cite [Kondo (2025)](https://doi.org/10.2151/sola.2025-028) in an appropriate way when you present and/or publish scientific results and products using this visualization and multivariate analysis method.

M. Kondo, 2025: RGB Hexagram Approach for Visualization and Multivariate Analysis with Application to Mixed-Phase Clouds, Scientific Online Letters on the Atmosphere, doi:10.2151/sola.2025-028, accepted.

### Overview of this repository
This repository provides a step-by-step tutorial for generating and visualizing the RGB Hexagram, a novel visualization method for multivariate analysis. The RGB Hexagram maps three normalized variables to the Red, Green, and Blue (RGB) color channels on a structured hexagonal grid, enabling intuitive interpretation of multivariate data distributions, especially in atmospheric science applications such as cloud microphysical analysis. 

#### Key Features

* Hexagonal RGB Grid Generation: Fortran programs (col_hex.f90, etc.) generate structured hexagonal color maps based on cyclic RGB assignment rules.

* Multivariate Mapping: Users can assign their own normalized variables (e.g., liquid water content, ice water content, vertical velocity) to RGB channels for visual analysis.

* Python Visualization: Python scripts read the Fortran output and generate color-mapped images with consistent x–y orientation and grid labeling.


# RGB Hexagram Tutorial
## What is this tutorial?

This tutorial demonstrates how to generate, visualize, and apply the **RGB Hexagram**—a novel colormap and multivariate analysis tool developed by Makoto Kondo (2025). The RGB Hexagram method maps **three variables** onto the Red, Green, and Blue color channels and arranges them in a **structured hexagonal grid**, allowing intuitive visualization of mixtures (1-, 2-, and 3-component combinations).

This tutorial is designed for:

- Researchers analyzing multivariate scientific data
- Visualization of cloud microphysics (e.g., liquid water, graupel, snow)
- Education in multivariate analysis techniques using Python and Fortran

This tutorial uses both **Fortran (for hexagram generation)** and **Python (for visualization and application with example data)**.


## File Structure
```
RGB_Hexagram_Tutorial/
├── fortran/
│ ├── col_hex.f90 # Fortran code to generate red-channel hexagram values
│ ├── col_hex_g.f90 # Fortran code to generate green-channel values
│ ├── col_hex_b.f90 # Fortran code to generate blue-channel values
│ ├── rw_hex_test_p.csv # Output: red channel array
│ ├── gw_hex_test_p.csv # Output: green channel array
│ ├── bw_hex_test_p.csv # Output: blue channel array
│ └── nw_hex_test_p.csv # Output: area index map (1 to 15)
├── python/
│ ├── tutorial_rgb_hexagram.ipynb # Main Jupyter Notebook tutorial
│ └── generate_rgb_hex.py # Python module to generate r/g/b/area arrays
├── LICENSE
└── README.md
```
    

---

## 3. Tutorial Workflow

### Step 1: Generate RGB Hexagram Arrays

You can choose between using the **Fortran program** or the **Python module** to generate the RGB hexagram arrays.

#### Option A: Using Fortran

```bash
cd fortran
gfortran col_hex.f90 -o col_hex
./col_hex   # Outputs rw_hex_test_p.csv etc.

```
## For python users
```
cd python
python
>>> from generate_rgb_hex import generate_rgb_hex
>>> r_hex, g_hex, b_hex, num_hex = generate_rgb_hex(k=11)
```
---
### Step 2: Visualize RGB Hexagram Structure

In the Jupyter Notebook tutorial_rgb_hexagram.ipynb, the following visualizations are included:

* RGB value distribution (r_hex, g_hex, b_hex)
* Area index map (num_hex)
* Composite RGB image based on the hexagram structure


You can visualize:

* Red/Green/Blue channel data separately
* Combined RGB colormap image
* Area indices for analysis


Step 3: Apply RGB Hexagram to 3D Data

The notebook also includes a section where random sample data (e.g., 3 subject scores) is:

* Normalized
* Mapped to RGB channels
* Positioned on the hexagram
* Visualized as frequency distributions

Example use cases:

* Mapping scientific variables to visualize dominant mixing states
* Tracking temporal evolution using additional vertical or time dimensions

---

## Reference
__ Kondo, M. (2025): RGB Hexagram Approach for Visualization and Multivariate Analysis with Application to Mixed-Phase Clouds. Scientific Online Letters on the Atmosphere (SOLA), accepted. __

------
    
### Requirements

The python module requires followings.

1. [Python3](https://www.python.org/)
2. [Numpy](https://pypi.org/project/numpy/)

### Tutorial

### Overview

The notebook [`RGB_hexagram_tutorial_for_generation.ipynb`](RGB_hexagram_tutorial_for_generation.ipynb) demonstrates how to:

- Create input CSV files containing RGB values on the RGB hexagram coordinate with an arbitrary coefficient k.
- Plot RGB hexagram figures based on the input data.
- Analysis and visualization for a sample of 3D data (test score of 3 subjects ) using an RGB hexagram.



A demonstration has been prepared in [tutorial/python](tutorial/python): [generate_rgb_hex.py](tutorial/python/generate_rgb_hex.py) provides a demonstration for each Red, Green, and Blue value on an RGB hexagram with coefficient k. First, please go to the tutorial directory.

```
$ cd tutorial/python
```

## Input File

The required input file is a CSV file, for example [`rw_hex_test_k2.csv`](sample/data/rw_hex_test_k2.csv), with the following format:

| x (center-x) | y (center-y) | R (0–1) | G (0–1) | B (0–1) |
|--------------|--------------|---------|---------|---------|
| ...          | ...          | ...     | ...     | ...     |

- `x`, `y`: Coordinates of the center of each hexagon.
- `R`, `G`, `B`: RGB color components to fill each hexagon (normalized to range [0, 1]).

## Requirements

This tutorial requires the following Python packages:

- numpy
- matplotlib
- pandas
- seaborn (optional, for styling)

You can install them using pip:

```bash
pip install numpy matplotlib pandas seaborn


Then, we explain the usage of class following the demonstrations.

### A tutorial of RGB hexagram for 3D data

Here is a case for fitting to pure PSVD data, included at [sample/data/psvd.csv](sample/data/psvd.csv). This sample data contains diameter (mm) and velocity (m/s) at first and second column, respectively. Therefore, the PSVD can be illustrated as follow.
