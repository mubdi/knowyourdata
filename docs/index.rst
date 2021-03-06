Welcome to KnowYourData
=======================
`KnowYourData` is a rapid and lightweight module to describe the statistics and structure of data arrays for interactive use. This project was started in 2018 and currently maintained by Mubdi Rahman.  This module arose from the regular need to display properties of data arrays while conducting data exploration or diagnostics, for instance, to set min and max values for plotting, or when looking at the first few values in an array don't provide a fair representation of the data. 

This module provides a quick way of displaying such information as the mean, median, confidence intervals, and size and shape of the data array.

The simplest way to use KnowYourData is to pass it a numpy array:

.. code-block:: python

   import numpy as np
   from knowyourdata import kyd

   # setting x as a numpy array
   x = np.random.randn(200)
   kyd(x)

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   quickstart
   installation
   usage


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
