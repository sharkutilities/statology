# -*- encoding: utf-8 -*-

"""
A Collection of Function to Treat Data Outliers

Outliers are extreme values that deviate from other observations on
data, they may indicate a variability in a measurement, or experimental
errors or a novelty. In other words, an outlier is an observation that
diverges from an overall pattern on a sample.

Outliers can be of two kinds: (I) univariate - typically found using
looking at the distribution of a single feature, and
(II) multivariate - determind by looking at the distributions of the
n-dimensional features.

An outlier can be treated using different methods:

    * **Trimming Method:** The outlier values are excluded from the
        analysis, and typically this is the fastest among others.
    * **Capping Method:** The outlier values are capped to a fixed
        value. This value may be determined based on the nature of the
        distribution of values.
    * **Discretization Method:** In this method, values are bucketized
        and assigned a value based on the discrete buckets.

Methods of Detection
--------------------

There are several different methods of detection of outliers, based on
the nature of distribution of the data. The popular methods are:

    * **IQR:** Inter-Quartile Range (IQR) is a popular method of
        detection and is particularly useful when the data is skewed.
    * **Z-Score:** Statistical method involving detection of outlier
        for normaly distributed values.
"""

import numpy as np
from scipy.stats import zscore

def quantile(array : np.ndarray, bounds : tuple = (0.25, 0.75)) -> np.ndarray:
    """
    A quick measure to identify outlier for an univariate series is
    by using the IQR value (as in box-plot) which states that any
    value in range :math:`[(Q1 - 1.5 * IQR), (Q3 + 1.5 * IQR)]` is
    not an outlier.
    """

    Q1, Q3 = np.quantile(array, bounds[0]), np.quantile(array, bounds[1])

    IQR = Q3 - Q1 # interquartile range, or the box length
    return np.array([
        (
            obs > (Q3 + 1.5 * IQR)
            or obs < (Q1 - 1.5 * IQR)
        )
        for obs in array
    ])


def zscore(array : np.ndarray, thresh : float = 2.0) -> np.ndarray:
    """
    The Z-Score is a statistical value that describes the data points
    and establishes an relationship around the feature mean.
    """

    scores = zscore(array)
    return np.array(list(map(lambda x : abs(x) > thresh, scores)))
