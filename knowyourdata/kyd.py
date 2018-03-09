import numpy as np


class KYD(object):
    """The Central Class for KYD"""

    # Variable for Data Vector
    data = None

    # Initial Flags
    f_allfinite = False
    f_hasnan = False
    f_hasinf = False

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

    def display(self, short=False):
        """Displaying all relevant statistics"""
        pass

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
