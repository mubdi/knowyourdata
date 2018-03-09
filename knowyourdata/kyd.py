import numpy as np
import sys


class KYD(object):
    """The Central Class for KYD"""

    # Variable for Data Vector
    data = None

    # Initial Flags
    f_allfinite = False
    f_hasnan = False
    f_hasinf = False

    # Display Settings
    col_width = 20

    def check_finite(self):
        """Checking to see if all elements are finite and setting flags"""
        if np.all(np.isfinite(self.data)):
            self.filt_data = self.data
            self.f_allfinite = True
        else:
            finite_inds = np.where(np.isfinite(self.data))
            self.filt_x = self.data[finite_inds]

            if np.any(np.isnan(self.data)):
                self.f_hasnan = True
            if np.any(np.isinf(self.data)):
                self.f_hasinf = True

    def check_struct(self):
        """Determining the Structure of the Numpy Array"""
        self.dtype = self.data.dtype
        self.ndim = self.data.ndim
        self.shape = self.data.shape
        self.size = self.data.size
        self.memsize = sys.getsizeof(self.data)

    def display_struct(self):
        """Display information about array structure"""

        pstr_list = []

        pstr_struct_header1 = "ARRAY STRUCTURE:"
        pstr_struct_header2 = "================="

        pstr_list.append(pstr_struct_header1)
        pstr_list.append(pstr_struct_header2)

        pstr_n_dim = (
            "Number of Dimensions:"
            "{self.ndim:>{self.col_width}}").format(
            self=self)
        pstr_list.append(pstr_n_dim)

        pstr_shape = (
            "Shape of Dimensions: "
            "{self.shape!s:>{self.col_width}}").format(
            self=self)
        pstr_list.append(pstr_shape)

        pstr_dtype = (
            "Array Data Type:     "
            "{self.dtype!s:>{self.col_width}}").format(
            self=self)
        pstr_list.append(pstr_dtype)

        pstr_memsize = (
            "Memory Size (bytes): "
            "{self.memsize:>{self.col_width}}").format(
            self=self)
        pstr_list.append(pstr_memsize)

        # Printing all Structure Parameters
        for pstr in pstr_list:
            print(pstr)

    def display(self, short=False):
        """Displaying all relevant statistics"""
        self.display_struct()

    def __init__(self, data):
        super(KYD, self).__init__()

        # Ensuring that the array is a numpy array
        if type(data) != np.ndarray:
            data = np.array(data)

        self.check_finite()

        self.data = data


def kyd(data, full_statistics=False):
    """Print statistics of any numpy array

    Keyword arguments:
    full_statistics -- printing all detailed statistics of the sources

    """

    data_kyd = KYD(data)
    if full_statistics:
        data_kyd.display()
    else:
        data_kyd.display(short=True)

    return data_kyd
