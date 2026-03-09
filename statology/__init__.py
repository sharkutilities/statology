# -*- encoding: utf-8 -*-

"""
A Collection of Statistical Function(s)

Statistics is the backbone of Data Science and Analytics and the
module exposes a simple collection of functions which acts as a
wrapper between external libraries like :mod:`numpy`,
:mod:`scipy.stats`, :mod:`pandas` etc. for a quick calculation.
"""

__version__ = "v1.3.0" # PEP-0440 Versioning Style

# init-time options registrations
from statology import average
from statology import outliers
from statology import normalize
