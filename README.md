# knowyourdata
A Simple Data Description Package for Python

[![Build Status](https://travis-ci.org/mubdi/knowyourdata.svg?branch=master)](https://travis-ci.org/mubdi/knowyourdata)
[![Build Status](https://scrutinizer-ci.com/g/mubdi/knowyourdata/badges/build.png?b=master)](https://scrutinizer-ci.com/g/mubdi/knowyourdata/build-status/master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/mubdi/knowyourdata/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/mubdi/knowyourdata/?branch=master)

A rapid and lightweight module to describe the statistics and structure of
data arrays for interactive use.

The most simple use case to display data is if you have a numpy array 'x':

    >>> from knowyourdata import kyd
    >>> kyd(x)


To Do:
------
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
* Have output specific for ipython environment vs. jupyter environment vs. non-interactive environment
* ~~For memory size, convert to human readable units~~
* Create simple options for graphs and the like

### Docs
* Write Sphinx Docs