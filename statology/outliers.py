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

Methods of Detection
--------------------

There are several different methods of detection of outliers, based on
the nature of distribution of the data. The popular methods are:

    * **IQR:** Inter-Quartile Range (IQR) is a popular method of
        detection and is particularly useful when the data is skewed.
    * **Z-Score:** Statistical method involving detection of outlier
        for normaly distributed values.

Methods of Treatment
--------------------

Once an outlier is detected, there are several possible ways of
treatment like:

    * **Trimming Method:** The outlier values are excluded from the
        analysis, and typically this is the fastest among others.
    * **Capping Method:** The outlier values are capped to a fixed
        value. This value may be determined based on the nature of the
        distribution of values.
    * **Discretization Method:** In this method, values are bucketized
        and assigned a value based on the discrete buckets.
"""

import numpy as np
from scipy.stats import zscore

def decorator(func : callable) -> callable:
    """
    The Base Decorator Function to Assert and Validate Elements

    The decorator wraps the function with a try-except block, and also
    asserts the value/dimensions in one place for better control.
    """

    def wrapper(xs : np.ndarray, bounds : float | tuple = None) -> np.ndarray:
        """
        The Wrapper on the Callable Function for the Decorator

        The wrapper checks the dimension of the boundary values, and
        asserts the value of the axis. The boundary and axis value are
        also imputed to the callable function.

        :type  xs: np.ndarray
        :param xs: The input array to be checked for outliers using
            different methods. This should be a numpy array, else the
            function tries to stack the same into an array.

        :type  bounds: float | tuple
        :param bounds: The boundary values that controls the outlier
            detection. Typically, this value should be a float meaning
            the outliers are to be treated and identified from both
            the left and right side of a normal distribution. However,
            if the value is a tuple, then the left and right side are
            given a different weightage. The decorator methods assigns
            the default value based on different function calls.
        """

        xs = np.array(xs) if not isinstance(xs, np.ndarray) else xs

        # ? default bounds are set in decorator based on function name
        default_bounds = dict(quartile = (0.25, 0.75), zscore = (-2.5, 2.5))

        bounds = default_bounds.get(func.__name__) if not bounds else bounds
        bounds = (float(-bounds), float(bounds)) if not \
            hasattr(bounds, "__iter__") else bounds

        assert len(bounds) == 2, f"Boundary should be 2D, got {len(bounds)}"
        return func(xs = xs, bounds = bounds)
    return wrapper

@decorator
def quartile(xs : np.ndarray, bounds : float | tuple = None) -> np.ndarray:
    """
    A quick measure to identify outlier for an univariate series is
    by using the IQR value (as in box-plot) which states that any
    value in range :math:`[(Q1 - 1.5 * IQR), (Q3 + 1.5 * IQR)]` is
    not an outlier.

    :type  xs: np.ndarray
    :param xs: The input array to be checked for outliers using
        different methods. This should be a numpy array, else the
        function tries to stack the same into an array.

    :type  bounds: float | tuple
    :param bounds: The boundary value that controls the outlier. The
        default setting is (0.25, 0.75) which means the outliers are
        bounded between :math:`[(Q1 - 1.5 * IQR), (Q3 + 1.5 * IQR)]`,
        but can now be controlled using a tuple.
    """

    lbound, rbound = np.quantile(xs, bounds[0]), np.quantile(xs, bounds[1])
    boundary_range = rbound - lbound

    return np.array([
        (
            obs > (rbound + 1.5 * boundary_range)
            or obs < (lbound - 1.5 * boundary_range)
        )
        for obs in xs
    ])


def zscore(array : np.ndarray, thresh : float = 2.0) -> np.ndarray:
    """
    The Z-Score is a statistical value that describes the data points
    and establishes an relationship around the feature mean.
    """

    scores = zscore(array)
    return np.array(list(map(lambda x : abs(x) > thresh, scores)))
