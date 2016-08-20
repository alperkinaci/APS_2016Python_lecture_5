'''
library of functions used in APS 2016 Python lecture 5

.. autosummary::

    peak_position
    center_of_mass
    fwhm
    interpolate
    taylorSeries

.. rubric:: Methods

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


def center_of_mass(x, y, b = [0.0]):
    '''
    report the center of mass of y(x)
    
    :param [float] x: array (list of float) of ordinates
    :param [float] y: array (list of float) of abcissae
    :param [float] b: array (list of float) of Taylor series coefficients
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
    
    The background, :math:`B`, is modeled as a polynomial (of arbitrary order :math:`m`).
    The polynomial coefficients are supplied in the variable. :math:`b`

    .. math::
        
        B = b_0 + b_1 x + b_2 x^2 + ... b_m x^m

    By default, there is only one coefficient so that 
    the background is a constant zero.
    A linear background may be supplied with a :math:`b` 
    array containing two values (constant, slope).
    '''
    # advanced homework
    #   first subtract a background
    # This can get complicated since one must assume an analytical model for the background.
    # Then, the task of fitting that model to the given data comes.
    # Both are advanced topics for lecture in this course series.
    # Let's assume a specific model: background to be subtracted is modeled by a Taylor series
    # AND further assume that it will be supplied by the caller,
    # AND assume a default constant value of zero.

    area_x_y_dy = 0
    area_y_dy = 0
    for i in range(1, len(y)):
        dx = x[i] - x[i-1]
        x_mean = (x[i] + x[i-1])/2
        background = taylorSeries(x_mean, b)
        y_mean = (y[i] + y[i-1])/2 - background
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


def taylorSeries(x, b = [0,]):
    '''
    evaluate a Taylor series expansion about :math:`x` using the supplied coefficients :math:`b`

    :param float x: value at which to evaluate Taylor series expansion
    :param [float] b: list of coefficients, default value is a constant, zero result
    :return float: :math:`T` (as shown below)
    
    The Taylor series expansion , :math:`T`, is based on the 
    supplied array of coefficients :math:`b` obtained from 
    previously fitting a polynomial.
    For a Taylor series of order :math:`m` 
    (with :math:`m+1` coefficients supplied), the polynomial expression is:

    .. math::
        
        T = b_0 + b_1 x + b_2 x^2 + ... b_m x^m
    
    Also expressed as a summation:

    .. math::
        
        T = {\sum_{i=0}^{i=m}b_i \\ x^i}
    
    Computationally, this can be re-arranged to avoid round-off, underflow,
    and/or overflow errors
    in the higher-order terms (as :math:`i` increases).  It is also faster
    since it does not generate powers of :math:`x`.  
    
    Factoring out the exponents:

    .. math::
        
        T = b_0 + x (b_1  + x (b_2 + x (b3 + x (b_m))))
    
    Finally, we write this as a procedure where
    :math:`i` progresses from the highest order term to the lowest
    (in effect, summing from the inside, high-order terms, out).
    Start with

    .. math::
        
        T = b_m
    
    Then loop :math:`i` from :math:`m-1` to :math:`0`, accumulating

    .. math::
        
        T = x \\ T + b_i
    
    For example, a Taylor series expansion to compute a constant zero
    will define ``b = [0,]`` which is the default.
    For a linear function, then ``b = [intercept, slope]``.
    '''
    T = b[-1]
    for b_i in reversed(b[:-1]):
        T = x * T + b_i
    return T
