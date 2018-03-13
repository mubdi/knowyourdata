Quickstart
==========

Installation is most easily done through ``pip``, which takes care of all required dependencies:

.. code-block:: bash

	pip install knowyourdata

The simplest way to use KnowYourData is to pass it a numpy array:

.. code-block:: python

   import numpy as np
   from knowyourdata import kyd

   # setting x as a numpy array
   x = np.random.randn(200)
   kyd(x)
