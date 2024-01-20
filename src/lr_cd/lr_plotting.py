# lr_plotting.py
# author: Jing Wen
# date: 2024-01-11

import numpy as np
import matplotlib.pyplot as plt

def plot_lr(X, y, intercept, coef):
    """Visualize the "lr_cd" linear regression model.

    This function takes actual data points and an estimated regression line,
    displaying them together in a scatter plot.
    
    Parameters
    ----------
    X: ndarray
        The observed data 'x', the independent variable
    
    y: ndarray
       The observed data 'y', the dependent variable. Both 'x' and 'y' should be continuous and of the same length.

    intercept: float
        Optimized intercept generated by 'lr_cd' function. 
        It will be used to calculate the estimated values using observed data 'x'.
    
    coef: ndarray
        Optimized coefficient weights vector.
        It will be used to calculate the estimated values using observed data 'x'.

    Returns
    -------
        A scatter plot of the observed data points overlayed with a line coming from the fitted weights.

    Examples
    --------
    >>> from lr_cd.lr_plotting import plot_lr
    >>> X = array([[0.69646919],
       [0.28613933],
       [0.22685145],
       [0.55131477],
       [0.71946897],
       [0.42310646],
       [0.9807642 ],
       [0.68482974],
       [0.4809319 ],
       [0.39211752]])
    >>> y = array([[6.34259481],
       [4.68506992],
       [4.54477713],
       [5.63500251],
       [6.45668483],
       [5.14153898],
       [6.8534962 ],
       [5.96761896],
       [5.88398172],
       [5.61370977]])
    >>> intercept = 0.42167642
    >>> coef = array([1.88190714])
    >>> plot_lr(X, y, intercept, coef)
    """
    # Check user inputs 
    if not isinstance(X, np.ndarray):
        raise TypeError("X must be a numpy array.")
    if not isinstance(y, np.ndarray):
        raise TypeError("y must be a numpy array.")
    if not isinstance(intercept, (float, int)):
        raise TypeError("intercept must be a float or an integer.")
    if not isinstance(coef, np.ndarray) or not np.issubdtype(coef.dtype, np.number):
        raise TypeError("coef must be a numpy array of numeric types.")
    
    # Check the dimensions of X and reshape if necessary
    if X.ndim == 1:
        X = X.reshape(-1, 1)
    if y.ndim == 1:
        y = y.reshape(-1, 1)
    
    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Calculate the estimated values using the intercept and coefficient
    y_pred = intercept + np.dot(X, coef)

    # Create a scatter plot of the observed data points on the axes object
    ax.scatter(X, y, color='blue', label='Observed data')

    # Plot the regression line
    ax.plot(X, y_pred, color='red', label='Fitted line')

    # Add title, labels and legends
    ax.set_title('Linear Regression Model')
    ax.set_xlabel('Independent variable (X)')
    ax.set_ylabel('Dependent variable (y)')
    ax.legend()

    return fig