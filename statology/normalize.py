# -*- encoding: utf-8 -*-

"""
A Set of Function to Perform Data Normalization on an ND-Array

A set of estimated function that scales and transforms a group of
data points individually such that it is in the given range on the
training set; e.g., between zero and one.
"""

import numpy as np

def minmax(xs : np.ndarray, fillna : float = 1.0) -> np.ndarray:
    """
    Performs min-max scaling, which is often used as an alternative
    to zero mean, unit variance scaling.

    :type  xs: np.ndarray
    :param xs: A set of independent feature values that needs to be
        scaled in a given feature range.

    :type  fillna: float
    :param fillna: Populate ``NaN`` values with this value, useful
        when there is only one data point, or all values are the same
        which returns ``ZeroDivisionError``. Defaults to 1.0 (max. of
        the feature range).

    .. math::
        :name: Min-Max Scaling

        xs =
            \begin{cases}
                1.0, (xs_{max} - xs_{min}) = 0 \\
                \frac{xs - xs_{min}}{xs_{max} - xs_{min}}
            \end{cases}

    The function provides an in-line manipulation of ``NaN`` values,
    and is modeled in a way that it can be directly applied like:

    .. code-block:: python

        import statology
        import pandas as pd

        data = pd.DataFrame(data = {
            "A" : ["A1", "A1", "A2", "A2", "A2"],
            "B" : ["B1", "B2", "B1", "B1", "B2"],
            "values" : list(range(1, 6))
        })

        f["normalized"] = f.groupby(["A", "B"])["values"].transform(
            lambda x : statology.normalize.minmax(x, fillna = 1.0)
        )

    In the above example, instead of performing a scaling operation
    on the feature ``values`` the function considers each group (A, B)
    as an individual function and performs scaling.
    """

    min_, max_ = xs.min(), xs.max()

    scaled = np.array([fillna] * xs.shape[0])
    if max_ - min_ > 0:
        scaled = (xs - min_) / (max_ - min_)

    return scaled


def normalize(xs : np.ndarray) -> np.ndarray:
    """
    Scale input vectors individually to unit norm (vector length), and
    return value of the same length as that of the unit vector.

    :type  xs: np.ndarray
    :param xs: A set of independent feature values that needs to be
        scaled in a given feature range.
    """

    return xs / np.sum(xs)
