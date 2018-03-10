from knowyourdata import kyd
import numpy as np


def test_struct():
    test_array = np.ones(5)
    data_summary = kyd(test_array)
    assert(data_summary.f_allfinite == True)
