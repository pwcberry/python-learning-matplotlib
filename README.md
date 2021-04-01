# Python Dojo: Pandas and Matplotlib

## Libraries for use in scientific research and in production for data science

### SciPy

- packages for computing math and science functions

## NumPy

- library of efficient matrices
- utilities for working with matrices
- fast functions
- randomization
- linear algebra
- Boolean indexing
- Slicing
- NumPy arrays (matrices & vectors & transformations)
- Array operations on each element
- `ufuncs` (`@np.vectorize`)

## Pandas

- hetereogeneous matrix-like data structures
- I/O tools
- labelled indices
- time series functionality
- slices and dices data
- statistical tools

- Dataframes

  - Every column is a Pandas series and have a label that can be accessed through the Dataframe
  - Every column share the same index
  - Can be sliced according to column or location `loc`
  - `pd.DataFrame(data = someData, columns = theColumns)`

- Time series: use `pytz` for timezone conversion
- Visualisations

## Matplotlib

- need `ipykernel` to run `matplotlib` from the command line... if you are running Ananconda or Jupyter Notebooks
- [convert pandas DataFrame to matplotlib table](https://pandas.pydata.org/docs/reference/api/pandas.plotting.table.html#pandas.plotting.table)
- DataFrame.style requires jinja2. Use pip or conda to install Jinja2
- When using `pyplot.show` or `pyplot.savefig` methods, this clears the plot buffer. To see the plot again, you will have to redraw it
- Don't use `%matplotlib inline` command in iPython otherwise the `pyplot` backend changes from the default (the system iPython is running on). This command is preferred for Jupyter notebooks
- What is a backend?

## AstroPy

## ASCL.net

- [redshifts](https://ascl.net/code/v/2821)
