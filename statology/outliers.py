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
from scipy import stats

def decorator(func : callable) -> callable:
    """
    The Base Decorator Function to Assert and Validate Elements

    The decorator wraps the function with a try-except block, and also
    asserts the value/dimensions in one place for better control.
    """

    def wrapper(xs : np.ndarray, bounds : float | tuple = None, **kwargs) -> np.ndarray:
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

        bounds = default_bounds.get(func.__name__) if not bounds else \
            (float(-bounds), float(bounds)) if not \
            hasattr(bounds, "__iter__") else bounds

        assert len(bounds) == 2, f"Boundary should be 2D, got {len(bounds)}"

        retvalue = func(xs = xs, bounds = bounds)

        # ? the following keyword argument controls are defined for
        # ? outlier data treatment methods: trimming, capping, etc.
        rtype = kwargs.get("rtype", bool) # return true/false array
        treat = kwargs.get("treatment", "capping") # treatment method

        if rtype != bool:
            iterable = zip(xs, retvalue)

            if treat == "trimming":
                retvalue = np.array([x for x, c in iterable if not c])
            elif treat == "capping":
                # ? set the capping value (static/clipping) value
                capping = kwargs.get("capping", np.nan)

                if not hasattr(capping, "__iter__"):
                    retvalue = np.array([
                        x if not c else capping for x, c in iterable
                    ])
                else:
                    retvalue = np.clip(xs, *capping)
            elif treat == "discretization":
                raise NotImplementedError("Apply Externally.")
            else:
                raise ValueError(f"Unknown Treatment Method: {treat}")

            retvalue = np.array(retvalue, dtype = rtype)
        else:
            pass # already boolean is returned by decorated function(s)

        return retvalue
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

    # the typically allowed values based on boundary condition::
    lrange = lbound - 1.5 * boundary_range
    rrange = rbound + 1.5 * boundary_range

    return (xs < lrange) | (xs > rrange)


@decorator
def zscore(xs : np.ndarray, bounds : float | tuple = None) -> np.ndarray:
    """
    The Z-Score is a statistical value that describes the data points
    and establishes an relationship around the feature mean. This
    method is helpful when the data is normally distrubuted.

    :type  xs: np.ndarray
    :param xs: The input array to be checked for outliers using
        different methods. This should be a numpy array, else the
        function tries to stack the same into an array.

    :type  bounds: float | tuple
    :param bounds: The boundary value that controls the outlier. The
        default setting is (-2.5, 2.5) which means the outliers are
        bounded between :math:`[-2.5, 2.5]` of the normal distribution,
        but can now be controlled using a tuple.
    """

    scores = stats.zscore(xs)
    return (scores < bounds[0]) | (scores > bounds[1])
