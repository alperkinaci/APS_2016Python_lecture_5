'''
library of functions used in APS 2016 Python lecture 5
'''

def _get_peak_index(y):
    '''
    report the index of the first point with maximum in y[i]
    
    :param [float] y: array of values
    :return int: index of y
    '''
    peak = max(y)
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
    # TODO: raise exception if x & y do not have same length
    # TODO: raise exception if x or y have zero length
    position = _get_peak_index(y)
    return x[position]


def center_of_mass(x, y):
    '''
    report the center of mass of y(x)
    
    :param [float] x: array of ordinates
    :param [float] y: array of abcissae
    :return float: center of mass
    
    .. math::
    
        C = \int_{-\infty}^{-\infty}{x y dx} / \int_{-\infty}^{-\infty}{y dx}
    
    x & y must have the same length
    '''
    # TODO: subtract a background
    area_x_y_dy = 0
    area_y_dy = 0
    for i in range(1, len(y)):
        dx = x[i] - x[i-1]
        x_mean = (x[i] + x[i-1])/2
        y_mean = (y[i] + y[i-1])/2
        area_x_y_dy += x_mean * y_mean * dx
        area_y_dy += y_mean * dx
    # TODO: what if area_y_dy is zero?
    return area_x_y_dy / area_y_dy


def fwhm(x, y):
    '''
    report the full-width at half-maximum of y(x)
    
    :param [float] x: array of ordinates
    :param [float] y: array of abcissae
    :return float: FWHM
    
    x & y must have the same length
    '''
    position = _get_peak_index(y)
    half_max = y[position] / 2
    
    # TODO: use linear interpolation
    # TODO: what if the data is noisy?
    
    # walk down the left side of the peak
    left = position
    while left > 0 and y[left] > half_max:
        left -= 1
    
    # walk down the right side of the peak
    right = position
    while right < len(y)-1 and y[right] > half_max:
        right += 1
    
    # computer FWHM
    return abs(x[left] - x[right])
