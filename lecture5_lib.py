'''
library of functions used in APS 2016 Python lecture 5

.. autosummary::

    peak_position
    center_of_mass
    fwhm

'''

def _get_peak_index(y):
    '''
    report the index of the first point with maximum in y[i]
    
    :param [float] y: array (list of float) of values
    :return int: index of y
    '''
    peak = max(y)
    # advanced homework
    # TODO: what if more than one point has the maximum value?
    return list(y).index(peak)


def peak_position(x, y):
    '''
    report the x value of the maximum in y(x)
    
    :param [float] x: array of ordinates
    :param [float] y: array of abcissae
    :return float: peak position
    
    x & y must have the same length
    '''
    # homework
    # TODO: raise IndexError exception if x & y arrays (lists) do not have same length
    # TODO: raise IndexError exception if x or y array (list) have zero length
    position = _get_peak_index(y)
    return x[position]


def center_of_mass(x, y):
    '''
    report the center of mass of y(x)
    
    :param [float] x: array (list of float) of ordinates
    :param [float] y: array (list of float) of abcissae
    :return float: center of mass
    
    The equation of the center of mass of :math:`y(x)`,

    .. math::
    
        C ={ \int_{-\infty}^{-\infty}{x \\ y \\ dx} \over \int_{-\infty}^{-\infty}{y \\ dx}}
    
    For a discrete set of :math:`n` ordered pairs of points,
    writing the math with the first point indicated by subscript 
    *zero* as in :math:`(x_0, y_0)`,

    .. math::
        
        C = {\sum_{i=1}^{i=n-1}(\\bar x \\ \\bar y \\ \Delta x) \over \sum_{i=1}^{i=n}(\\bar y \\ \Delta x)}
    
    where :math:`\Delta x = x_i - x_{i-1}`, :math:`\\bar{x} = (x_i + x_{i-1})/2`, 
    and :math:`\\bar{y} = (y_i + y_{i-1})/2`.
    
    x & y must have the same length
    '''
    # advanced homework
    # TODO: first subtract a background
    area_x_y_dy = 0
    area_y_dy = 0
    for i in range(1, len(y)):
        dx = x[i] - x[i-1]
        x_mean = (x[i] + x[i-1])/2
        y_mean = (y[i] + y[i-1])/2
        area_x_y_dy += x_mean * y_mean * dx
        area_y_dy += y_mean * dx
    
    # homework
    # - Describe what happens when area_y_dy is zero
    return area_x_y_dy / area_y_dy


def fwhm(x, y):
    '''
    report the full-width at half-maximum of y(x)
    
    Start at the peak position and walk down each side, 
    stopping at the first point where *y* value is less than or equal
    to the peak *y* value.  The difference between the *x* values
    of the two sides is the FWHM.
    
    :param [float] x: array of ordinates
    :param [float] y: array of abcissae
    :return float: FWHM
    
    x & y must have the same length
    '''
    position = _get_peak_index(y)
    half_max = y[position] / 2
    
    # homework
    # - Describe what happens when the data are noisy?
    # This algorithm uses the first data to fall below the half_max.
    # Which may result in a reported FWHM that is smaller than the actual value.
    # To improve accuracy in this case, additional curve fitting would be needed.
    
    # walk down the left side of the peak
    left = position
    # homework
    #   make sure that "left" will not advance too far, out of range of the indexes
    while left > 0 and y[left] > half_max:
        left -= 1
    
    # walk down the right side of the peak
    right = position
    while right < len(y)-1 and y[right] > half_max:
        right += 1
    
    # compute FWHM
    # advanced homework
    #  use linear interpolation to improve precision
    x_left = interpolate(half_max, y[left], x[left], y[left+1], x[left+1])
    x_right = interpolate(half_max, y[right], x[right], y[right-1], x[right-1])
    return abs(x_left - x_right)


def interpolate(x, x1, y1, x2, y2):
    '''
    given data points x1,y1 & x2,y2, find y given x using linear interpolation
    '''
    return y1 + (y2 - y1)*(x - x1)/(x2 - x1)
