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

    def get_basic_stats(self):
        """Get basic statistics about array"""
        self.min = np.min(self.filt_data)
        self.max = np.max(self.filt_data)
        self.range = self.max - self.min
        self.mean = np.mean(self.filt_data)
        self.std = np.std(self.filt_data)
        self.median = np.median(self.filt_data)
        self.firstquartile = np.percentile(self.filt_data, 25)
        self.thirdquartile = np.percentile(self.filt_data, 75)
        self.cl_99 = np.percentile(self.filt_data, np.array([0.5, 99.5]))
        self.cl_95 = np.percentile(self.filt_data, np.array([2.5, 97.5]))
        self.cl_68 = np.percentile(self.filt_data, np.array([16.0, 84.0]))

    def display_basic_stats(self):
        """Display basic statistics of array"""
        pstr_list = []

        pstr_struct_header1 = '\033[1m' + "Basic Statistics  " + '\033[0m'

        pstr_list.append(pstr_struct_header1)

        pstr_meanstdhead = (
            "\n"
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

        pstr_3pthead = (
            "\n"
            "{0:^10}"
            "{1:^10}"
            "{2:^10}"
            "{3:^10}"
            "{4:^10}"
        ).format('Min,', '1Q', 'Median', '3Q', 'Max')
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

        pstr_clhead = (
            "\n"
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
            "Number of Dimensions:"
            "{self.ndim:>15}").format(
            self=self)
        pstr_list.append(pstr_n_dim)

        pstr_shape = (
            "Shape of Dimensions: "
            "{self.shape!s:>15}").format(
            self=self)
        pstr_list.append(pstr_shape)

        pstr_dtype = (
            "Array Data Type:     "
            "{self.dtype!s:>15}").format(
            self=self)
        pstr_list.append(pstr_dtype)

        pstr_memsize = (
            "Memory Size (bytes): "
            "{self.memsize:>15}").format(
            self=self)
        pstr_list.append(pstr_memsize)

        return pstr_list

    def display(self, short=False):
        """Displaying all relevant statistics"""
        print()
        pstr_basic = self.display_basic_stats()
        pstr_struct = self.display_struct()

        l_colwidth = 0
        for string1 in (pstr_basic):
            if len(string1) > l_colwidth:
                l_colwidth = len(string1)
        l_colwidth += 1

        r_colwidth = 0
        for string1 in (pstr_basic):
            if len(string1) > r_colwidth:
                r_colwidth = len(string1)

        # new_colwidth = self.col_width + 20

        # Finding the longest string
        len_list = max([len(pstr_basic), len(pstr_struct)])

        for i in range(len_list):
            tmp_str = ''
            if i < len(pstr_basic):
                tmp_str += (pstr_basic[i].ljust(l_colwidth))
            else:
                tmp_str += ''.ljust(l_colwidth)
            tmp_str += ' | '
            if i < len(pstr_struct):
                tmp_str += (pstr_struct[i]).ljust(r_colwidth)

            print(tmp_str)

        print()

    def __init__(self, data):
        super(KYD, self).__init__()

        # Ensuring that the array is a numpy array
        if type(data) != np.ndarray:
            data = np.array(data)

        self.data = data

        self.check_finite()
        self.check_struct()
        self.get_basic_stats()


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
