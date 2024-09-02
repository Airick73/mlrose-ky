"""Neural network activation functions."""

import warnings

import numpy as np

# Authors: Genevieve Hayes (modified by Andrew Rollings, Kyle Nakamura)
# License: BSD 3-clause
from mlrose_ky.decorators import short_name

warnings.filterwarnings("ignore")


@short_name("identity")
def identity(x, deriv=False):
    """Linear activation function

    Parameters
    ----------
    x: np.ndarray
        Array containing input data.

    deriv: bool, default: False
        Whether to return the function or its derivative.
        Set True for derivative.

    Returns
    -------
    fx: np.ndarray
        Value of activation function at x
    """
    if not deriv:
        fx = x
    else:
        fx = np.ones(np.shape(x))

    return fx
