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
    if len(x) != len(y):
        raise IndexError('x & y arrays not of the same length, cannot assume ordered pairs')
    if len(x) == 0: # no need to test both since we know now they have same length
        raise IndexError('arrays have zero length, no data')
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
    # lecture5_lib.py:83: RuntimeWarning: divide by zero encountered in double_scalars
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
    # - Describe what happens when the data is noisy?
    # advanced homework
    # TODO: use linear interpolation to improve precision
    
    # walk down the left side of the peak
    left = position
    while y[left] > half_max:
        left -= 1
    # homework
    # TODO: make sure that "left" will not advance too far, out of range of the indexes
    # otherwise, y[-1] will generate an exception
    # This chart shows an example when this would happen
    # http://usaxs.xray.aps.anl.gov/livedata/specplots/2010/04/04_25/s00095.png
    
    # walk down the right side of the peak
    right = position
    while right < len(y)-1 and y[right] > half_max:
        right += 1
    
    # compute FWHM
    return abs(x[left] - x[right])
