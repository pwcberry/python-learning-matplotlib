# Python Dojo: pandas and matplotlib

The code in this repository serves as an introduction to two data-oriented libraries **matplotlib** and **pandas**. It is intended to give readers a sample of the possibilities in data analysis and data visualisation that these libraries offer.

The libraries NumPy and AstroPy are also introduced to demonstrate the range of uses for matplotlib.

What should be obtained through the analysis and visualisations of data is a compelling story.

## The Code Examples

The examples are found in as Jupyter Notebooks in the folder `notebooks` and are indexed in order of complexity. They can be run on any Python system that has a Jupyter server or even run inside Visual Studio Code with the Jupyter and Python extensions. Essentially, to execute code with matplotlib, the `ipykernel` module must be installed on your system.

If you don't have Jupyter installed, here is some information to help you get started:

- [Anaconda](https://www.anaconda.com/products/individual)
- [Jupyter extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [Python extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

You can install the libraries needed to run the examples by running the following at the root of this repo:

```
python -m pip install -r requirements.txt
```

And if the above haven't installed it, you should also:

```
python -m pip install ipykernel
```

as this is required by `matplotlib`.

## An Overview of the Libraries

pandas and matplotlib are found extensively in the data science and scientific research communities. matplotlib itself is a foundation library for other, more feature-rich libraries.

### NumPy

[Website](https://numpy.org/)

This library allows for efficient creation, querying and manipulation of arrays and matrices. It also provides:

- Fast mathematical functions
- Random number generators
- Linear algebra operations
- Boolean indexing

### pandas

[Website](https://pandas.pydata.org/)

This library supports heterogeneous, matrix-like, data structures that can be sourced from data formats such as CSV, Excel and SQL databases. It also provides:

- I/O tools
- labelled indices
- time-series functionality
- statistical tools
- filtering and other data manipulation tools
- operations to plot data

The key data structures the library supports are the `DataFrame` and `Series`.

#### `DataFrame`

[Docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)

- Two-dimensional tabular data
- Contains labelled axes
- Supports operations such as slicing, filtering and grouping
- Built from `Series` objects

#### `Series`

[Docs](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)

- One-dimensional array built from numpy's array
- Statistical methods
- Methods to determine missing values
- Data type conversion
- Boolean operations
- Arithmetic operations

### matplotlib

[Website](https://matplotlib.org/stable/index.html)

A comprehensive library for creating static, animated or interactive visualisations.

You can plot:

- bar charts
- line charts
- histograms
- scatter plots
- contour plots
- 3d plots

This is has quite a low-level API. You can control:

- figure titles, including font and color
- marker styles
- line colours
- fill colours
- histogram gradients

With the [Seaborn library](https://seaborn.pydata.org/) you can even plot according to themes. See [the matplotlib website](https://matplotlib.org/stable/thirdpartypackages/index.html) for a summary of third-party packages that extend this library.

### astropy

[Website](https://www.astropy.org/)

A project to develop core packages for astronomy. These packages provide:

- classes to determine positions in the sky according to locations on earth, or from the vantage of the galactic centre
- operations that work on angles
- cosmological functions
- objects to handle the various units found in astrometry and astrophysics

## Provenance of the data

The data that is included in this repository is sourced from public locations on the Internet. However, to keep this repo small, the data has been pre-processed to keep file sizes small.

| File | Description | Source |
| --- | --- | --- |
| `Melbourne_Annual.csv` | Annual mean temperatures and total rainfalls | [Bureau of Meterology](https://www.bom.gov.au/climate/data/) |
| `BOM_VIC_20210323.xlsx` | Daily temperatures and rainfall totals for Melbourne | [Bureau of Meterology](https://www.bom.gov.au/climate/data/) |
| `NGC-IC.xlsx` | Objects listed in the New General Catalog and Index Catalog of non-stellar objects | Uncertain; but a starting point is [NASA - HEASARC](https://heasarc.gsfc.nasa.gov/W3Browse/all/ngc2000.html). A related project is [The NGC/IC Project](http://ngcicproject.observers.org) |
| `star-clusters.csv` | Milky Way Star Clusters Catalog | [NASA - HEASARC](https://heasarc.gsfc.nasa.gov/W3Browse/all/mwsc.html) |
| `stars.csv` | Star catalog derived from Hipparcos data | [VizieR - The Hipparcos Catalog](http://cdsarc.unistra.fr/viz-bin/cat/I/239) |
| `stars-849.csv` | Derived from `stars.csv` | |
| `abell-galaxy-clusters-simplified.csv` | Abell Catalog of Clusters of Galaxies | [NASA - HEARSAC](https://heasarc.gsfc.nasa.gov/W3Browse/all/abell.html) |

In the `scripts` folders are some of the python scripts I ran to reduce the source data into the examples found in this repo.
