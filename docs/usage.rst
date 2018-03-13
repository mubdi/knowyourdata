Usage
=====

The simplest way to use KnowYourData is to pass it a numpy array:

.. code-block:: python

   import numpy as np
   from knowyourdata import kyd

   # setting x as a numpy array
   x = np.random.randn(200)
   kyd(x)

The ``kyd`` function returns a structure that contains the information extracted from the data array. You can access this information through:

.. code-block:: python

	info_x = kyd(x)

	# The Third Quartile of x:
	print(info_x.thirdquartile)