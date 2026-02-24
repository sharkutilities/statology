# -*- encoding: utf-8 -*-

"""
A Set of Function(s) to Aggregate Array based on a Logic

A simple example of aggregation is the statistical measures like
:attr:`mean`, :attr:`median`, etc. Additional in-frequently but
popular aggregation functions are defined here for end-users.
"""

import numpy as np
from typing import Union, Callable

def weighted(
        xs : np.ndarray,
        initial : float,
        rate : Union[float, Callable],
        decay : bool = True,
        nforecast : int = 1,
        moving : bool = True,
        returnscalar : bool = True
    ) -> float:
    """
    Collate a Series based on Weighted Moving Average (WMA) Method

    WMA is a variant of SMA/EMA, and is popularly used in financial
    analysis, which gives more weightage to the recent data and
    produces a smoother line (sometimes) giving a more accurate picture
    of the underlying data trend.

    :type  xs: np.ndarray
    :param xs: The input data array which is multiplied against a
        weight values by creating a factors of same shape as the
        input array. The function gives the flexibility to work for
        an n-dimensional :mod:`numpy` array based on length.

    :type  initial: float
    :param initial: The initial weighteage of the value, typically
        a value of :attr:`0.5` is a good starting point.

    :type  rate: float, callable
    :param rate: The rate at which subsequent values are increasing
        or decreasing. Typically, a value of :attr:`2` (i.e., at each
        subsequent level the impact is halved - "half life decay") is
        a good starting point. The rate can either be a numeric value,
        i.e., each subsequent values is calculated as
        :attr:`n_1 = n_0 / rate` or can be a callable, i.e., each
        value is calculated like :attr:`n_1 = rate(n_0)` thus allow
        more control and dynamic approach.

    :type  decay: bool
    :param decay: When true (default) the returned array will be
        reveresed, i.e., it will give more priority to the recent
        data points (where the :attr:`x` is sorted in ascending order),
        else typically returns a "growth" array where more weightage
        is given to the data which is older.

    :type  nforecast: int
    :param nforecast: Number of points to forecast based on the moving
        average calculation, defaults to 1. Combine this with the
        ``moving`` to calculate weighted moving average forecast for
        the given series.

    :type  moving: bool
    :param moving: Toogle to move/shift the series in the forward
        calculation method, defaults to True. This method is only
        applicable to one dimensional array.

    :type  returnscalar: bool
    :param returnscalar: Return a scalar value instead of an array,
        typically useful, when the length of forecast ``nforecast``
        is one, this will return one value, default.
    """

    factors = [initial] # append the initial values, and then calculate
    for _ in range(len(xs) - 1):
        factors.append(
            rate(factors[-1]) if hasattr(rate, "__call__")
            else factors[-1] / rate
        )

    factors = np.array(factors)

    # ..versionadded:: v1.2.1 check data quality, raise error
    assert (
        (xs.ndim == 1 and nforecast > 1)
        or (nforecast == 1)
    ), f"Only 1-D is Supported for N-Forecast >= 1, got {xs.ndim}"

    assert (
        (returnscalar and nforecast == 1)
        or (not returnscalar and nforecast >= 1)
    ), f"Return Scalar = {returnscalar} and N-Forcast = {nforecast}"

    forecasts = []
    for _ in range(nforecast):
        forecast = np.sum((factors[::-1] if not decay else factors) * xs)
        forecasts.append(forecast)

        if moving:
            xs = np.append(xs[1:], forecast)
        else:
            continue

    forecasts = np.array(forecasts)
    return forecasts[0] if returnscalar else forecasts
