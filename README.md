# Introduction
This software provides sample source code as a tutorial for applying the RGB (Red, Green, and Blue) hexagram, a visualization and multivariate analysis method, to 3D and higher-dimensional data.
The supported languages are now Python and fortran.  If you are a fortran user and you want to use fortran codes, please contact me with the e-mail address in [ORCID](https://orcid.org/0000-0003-4434-7877).

Please see [Kondo (2025)](https://doi.org/10.2151/sola.2025-028) for details of the visualization and multivariate analysis method.

# Licence and agreement
The source codes is distributed under the [MIT license](https://opensource.org/licenses/MIT).  
You must cite [Kondo (2025)](https://doi.org/10.2151/sola.2025-028) in an appropriate way when you present and/or publish scientific results and products using this visualization and multivariate analysis method.

M. Kondo, 2025: RGB Hexagram Approach for Visualization and Multivariate Analysis with Application to Mixed-Phase Clouds, Scientific Online Letters on the Atmosphere, doi:10.2151/sola.2025-028, accepted.

# For python users

## Requirements

The python module requires followings.

1. [Python3](https://www.python.org/)
2. [Numpy](https://pypi.org/project/numpy/)

## Tutorial

A demonstration has been prepared in [sample/python](sample/python): [psvd.py](sample/python/psvd.py) and [psvd_bin.py](sample/python/psvd_bin.py) provides a demonstration for pure PSVD data and a demonstration for binned PSVD data, respectively. First, please go to the sample directory.

```
$ cd tutorial/python
```

Then, we explain the usage of class following the demonstrations.

### A case for pure PSVD data

Here is a case for fitting to pure PSVD data, included at [sample/data/psvd.csv](sample/data/psvd.csv). This sample data contains diameter (mm) and velocity (m/s) at first and second column, respectively. Therefore, the PSVD can be illustrated as follow.
