from knowyourdata import kyd
import numpy as np


def test_struct():
    test_array = np.ones(5)
    data_summary = kyd(test_array)
    assert(data_summary.f_allfinite == True)


def test_int_data():
    test_array = np.ones(5, dtype=np.int32)
    data_summary = kyd(test_array)
    assert(data_summary.dtype.name == 'int32')


def test_all_nan():
    test_array = np.ones(5) * np.nan
    data_summary = kyd(test_array)