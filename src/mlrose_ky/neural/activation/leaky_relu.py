"""Neural network activation functions."""

import warnings

import numpy as np

# Authors: Genevieve Hayes (modified by Andrew Rollings, Kyle Nakamura)
# Contributor : Ankit Grover
# License: BSD 3-clause
from mlrose_ky.decorators import short_name

warnings.filterwarnings("ignore")


@short_name("leaky_relu")
def leaky_relu(x, alpha=0.3, deriv=False):
    """Leaky ReLU activation function

    Parameters
    ----------
    x: np.ndarray
        Array containing input data.
    alpha: int , default : 0.3
        Alpha value to be set for applying small negative gradient
    deriv: bool, default: False
        Whether to return the function or its derivative.
        Set True for derivative.

    Returns
    -------
    fx: np.ndarray
        Value of activation function at x
    """
    fx = np.copy(x)
    fx = np.where(fx < 0, fx * alpha, fx)

    if deriv:
        fx[np.where(fx > 0)] = 1
        fx[np.where(fx < 0)] = alpha

    return fx
