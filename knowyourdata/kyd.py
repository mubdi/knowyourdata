"""
KnowYourData
============

A rapid and lightweight module to describe the statistics and structure of
data arrays for interactive use.

The most simple use case to display data is if you have a numpy array 'x':

    >>> from knowyourdata import kyd
    >>> kyd(x)

"""

import sys
import numpy as np


class KYD(object):
    """The Central Class for KYD"""

    # Variable for Data Vector
    data = None

    # Initial Flags
    f_allfinite = False
    f_allnonfinite = False
    f_hasnan = False
    f_hasinf = False

    # Display Settings
    col_width = 10
    precision = 4

    def check_finite(self):
        """Checking to see if all elements are finite and setting flags"""
        if np.all(np.isfinite(self.data)):
            self.filt_data = self.data
            self.f_allfinite = True
        else:
            finite_inds = np.where(np.isfinite(self.data))

            self.filt_data = self.data[finite_inds]

            if self.filt_data.size == 0:
                self.f_allnonfinite = True

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
        self.human_memsize = sizeof_fmt(self.memsize)

    def get_basic_stats(self):
        """Get basic statistics about array"""

        if self.f_allnonfinite:
            self.min = self.max = self.range = np.nan
            self.mean = self.std = self.median = np.nan
            self.firstquartile = self.thirdquartile = np.nan
            self.cl_68 = self.cl_95 = self.cl_99 = np.array([np.nan, np.nan])

            return

        self.min = np.float_(np.min(self.filt_data))
        self.max = np.float_(np.max(self.filt_data))
        self.range = self.max - self.min
        self.mean = np.mean(self.filt_data)
        self.std = np.std(self.filt_data)
        self.median = np.float_(np.median(self.filt_data))
        self.firstquartile = np.float_(np.percentile(self.filt_data, 25))
        self.thirdquartile = np.float_(np.percentile(self.filt_data, 75))
        self.cl_99 = np.float_(
            np.percentile(self.filt_data, np.array([0.5, 99.5])))
        self.cl_95 = np.float_(
            np.percentile(self.filt_data, np.array([2.5, 97.5])))
        self.cl_68 = np.float_(
            np.percentile(self.filt_data, np.array([16.0, 84.0])))

    def display_basic_stats(self):
        """Display basic statistics of array"""
        pstr_list = []

        # Heading for Section

        pstr_struct_header1 = '\033[1m' + "Basic Statistics  " + '\033[0m'
        pstr_struct_header2 = ''

        pstr_list.append(pstr_struct_header1)
        pstr_list.append(pstr_struct_header2)

        # Mean and Standard Deviation

        pstr_meanstdhead = (
            "{0:^15}"
            "{1:^15}"
        ).format("Mean", "Std Dev")
        pstr_meanstdhead = (
            "{0:^{self.col_width}}"
        ).format(pstr_meanstdhead, self=self)
        pstr_list.append(pstr_meanstdhead)

        pstr_meanstdstat = (
            "{self.mean:^15.{self.precision}}"
            "{self.std:^15.{self.precision}}"
        ).format(self=self)
        pstr_meanstdstat = (
            "{0:^{self.col_width}}"
        ).format(pstr_meanstdstat, self=self)
        pstr_list.append(pstr_meanstdstat)

        pstr_list.append("")

        # Three point statistics

        pstr_3pthead = (
            "{0:^10}"
            "{1:^10}"
            "{2:^10}"
            "{3:^10}"
            "{4:^10}"
        ).format('Min', '1Q', 'Median', '3Q', 'Max')
        pstr_3pthead = (
            "{0:^{self.col_width}}"
        ).format(pstr_3pthead, self=self)
        pstr_list.append(pstr_3pthead)

        pstr_3ptstat = (
            "{self.min:^10.{self.precision}}"
            "{self.firstquartile:^10.{self.precision}}"
            "{self.median:^10.{self.precision}}"
            "{self.thirdquartile:^10.{self.precision}}"
            "{self.max:^10.{self.precision}}"
        ).format(self=self)
        pstr_3ptstat = (
            "{0:^{self.col_width}}"
        ).format(pstr_3ptstat, self=self)
        pstr_list.append(pstr_3ptstat)

        pstr_list.append("")

        # Confidence Levels

        pstr_clhead = (
            "{0:^10}"
            "{1:^10}"
            "{2:^10}"
            "{3:^10}"
            "{4:^10}"
            "{5:^10}"
        ).format('-99 CL', '-95 CL', '-68 CL', '+68 CL', '+95 CL', '+99 CL')
        pstr_clhead = (
            "{0:^{self.col_width}}"
        ).format(pstr_clhead, self=self)
        pstr_list.append(pstr_clhead)

        pstr_clstat = (
            "{self.cl_99[0]:^10.{self.precision}}"
            "{self.cl_95[0]:^10.{self.precision}}"
            "{self.cl_68[0]:^10.{self.precision}}"
            "{self.cl_68[1]:^10.{self.precision}}"
            "{self.cl_95[1]:^10.{self.precision}}"
            "{self.cl_99[1]:^10.{self.precision}}"
        ).format(self=self)
        pstr_clstat = (
            "{0:^{self.col_width}}"
        ).format(pstr_clstat, self=self)
        pstr_list.append(pstr_clstat)

        return pstr_list

    def display_struct(self):
        """Display information about array structure"""

        pstr_list = []

        # pstr_struct_header0 = "................."
        pstr_struct_header1 = '\033[1m' + "Array Structure  " + '\033[0m'
        pstr_struct_header2 = "                 "

        # pstr_list.append(pstr_struct_header0)
        pstr_list.append(pstr_struct_header1)
        pstr_list.append(pstr_struct_header2)

        pstr_n_dim = (
            "Number of Dimensions:\t"
            "{self.ndim}").format(
                self=self)
        pstr_list.append(pstr_n_dim)

        pstr_shape = (
            "Shape of Dimensions:\t"
            "{self.shape}").format(
                self=self)
        pstr_list.append(pstr_shape)

        pstr_dtype = (
            "Array Data Type:\t"
            "{self.dtype}").format(
                self=self)
        pstr_list.append(pstr_dtype)

        pstr_memsize = (
            "Memory Size:\t\t"
            "{self.human_memsize}").format(
                self=self)
        pstr_list.append(pstr_memsize)

        return pstr_list

    def display(self, short=False):
        """Displaying all relevant statistics"""

        if short:
            pass

        print("")
        pstr_basic = self.display_basic_stats()
        pstr_struct = self.display_struct()
        n_basic = len(pstr_basic)
        n_struct = len(pstr_struct)

        l_colwidth = max([len(x) for x in pstr_basic]) + 1

        r_colwidth = max([len(x) for x in pstr_struct]) + 2

        # new_colwidth = self.col_width + 20

        # Finding the longest string
        len_list = max([n_basic, n_struct])

        for i in range(len_list):
            tmp_str = '| '
            if i < n_basic:
                tmp_str += (pstr_basic[i].ljust(l_colwidth))
            else:
                tmp_str += ''.ljust(l_colwidth)
            tmp_str += '\t| '

            if i < n_struct:
                tmp_str += (pstr_struct[i].expandtabs().ljust(r_colwidth))
            else:
                tmp_str += ''.ljust(r_colwidth)
            tmp_str += '\t|'

            print(tmp_str)

        print("")

    def clear_memory(self):
        """Ensuring the Numpy Array does not exist in memory"""
        del self.data
        del self.filt_data

    def __init__(self, data):
        super(KYD, self).__init__()

        # Ensuring that the array is a numpy array
        if not isinstance(data, np.ndarray):
            data = np.array(data)

        self.data = data

        self.check_finite()
        self.check_struct()
        self.get_basic_stats()
        self.clear_memory()


def sizeof_fmt(num, suffix='B'):
    """Return human readable version of in-memory size.
    Code from Fred Cirera from Stack Overflow:
    https://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size
    """
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def kyd(data, full_statistics=False):
    """Print statistics of any numpy array

    data -- Numpy Array of Data

    Keyword arguments:
    full_statistics -- printing all detailed statistics of the sources
    (Currently Not Implemented)

    """

    data_kyd = KYD(data)
    if full_statistics:
        data_kyd.display()
    else:
        data_kyd.display(short=True)

    return data_kyd
