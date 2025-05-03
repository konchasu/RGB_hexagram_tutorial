# Introduction
This software provides sample source code as a tutorial for applying the RGB (Red, Green, and Blue) hexagram, a visualization and multivariate analysis method, to 3D and higher-dimensional data.
The supported languages are now Python and fortran.  If you are a fortran user and you want to use fortran codes, please contact me with the e-mail address in [ORCID](https://orcid.org/0000-0003-4434-7877).

Please see [Kondo (2025)](https://doi.org/10.2151/sola.2025-028) for details of the visualization and multivariate analysis method.

# Licence and agreement
The source codes are distributed under the [MIT license](https://opensource.org/licenses/MIT).  
You must cite [Kondo (2025)](https://doi.org/10.2151/sola.2025-028) in an appropriate way when you present and/or publish scientific results and products using this visualization and multivariate analysis method.

M. Kondo, 2025: RGB Hexagram Approach for Visualization and Multivariate Analysis with Application to Mixed-Phase Clouds, Scientific Online Letters on the Atmosphere, doi:10.2151/sola.2025-028, accepted.

# For python users

## Requirements

The python module requires followings.

1. [Python3](https://www.python.org/)
2. [Numpy](https://pypi.org/project/numpy/)

## Tutorial

## Overview

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
