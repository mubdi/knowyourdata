[![Build Status](https://travis-ci.org/mubdi/knowyourdata.svg?branch=master)](https://travis-ci.org/mubdi/knowyourdata)
[![Build Status](https://scrutinizer-ci.com/g/mubdi/knowyourdata/badges/build.png?b=master)](https://scrutinizer-ci.com/g/mubdi/knowyourdata/build-status/master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/mubdi/knowyourdata/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/mubdi/knowyourdata/?branch=master)
[![Documentation Status](https://readthedocs.org/projects/knowyourdata/badge/?version=latest)](http://knowyourdata.readthedocs.io/en/latest/?badge=latest)

# KnowYourData
A Simple Data Description Package for Python. 

A rapid and lightweight module to describe the statistics and structure of data arrays for interactive use. This project was started in 2018 and currently maintained by Mubdi Rahman.  

## Installation

### Dependencies 
KnowYourData requires: 

* Python (>=2.7 or >=3.4)
* Numpy (>=1.10.0)
* ipython

### User Installation
The easiest way to install KnowYourData is with `pip`:

	pip install knowyourdata 

## Usage 

For full usage, details are available in the [documentation](http://knowyourdata.readthedocs.io/). The most simple use case to display data is if you have a numpy array 'x':

    >>> from knowyourdata import kyd
    >>> kyd(x)

## Help and Support
* Documentation: <http://knowyourdata.readthedocs.io/>


Development To Do:
------------------
### Data Support
* **Add support for Pandas**
* Add support for masked arrays
* Add support for record arrays
* Allow n-dimensional arrays 
* Special support for boolean arrays
* ~~Special support for complex arrays~~

### Statistics
* ~~Add basic statistics (mean, std deviation, median, quartiles)~~

### Display
* ~~Have output specific for ipython environment vs. jupyter environment vs. non-interactive environment~~
* ~~For memory size, convert to human readable units~~
* Create simple options for graphs and the like

### Docs
* ~~Write Sphinx Docs~~