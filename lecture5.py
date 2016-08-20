'''
Python code used in APS 2016 Python lecture 5
'''

import h5py
import lecture5_lib

def main():
    ''' '''
    f = h5py.File('writer_1_3.hdf5', 'r')
    x = f['/Scan/data/two_theta']
    y = f['/Scan/data/counts']
    print 'file:', f.filename
    print 'peak position:', lecture5_lib.peak_position(x, y)
    print 'center-of-mass:', lecture5_lib.center_of_mass(x, y)
    background_parameters = (500, 2.1)  # completely made-up, not derived from any fit
    print 'center-of-mass:', lecture5_lib.center_of_mass(x, y, background_parameters)
    slope = (y[-1] - y[0]) / (x[-1] - x[0])
    intercept = lecture5_lib.interpolate(0.0, x[0], y[0], x[-1], y[-1])
    background_parameters = (intercept, slope)  # straight line between first and last points
    print 'center-of-mass:', lecture5_lib.center_of_mass(x, y, background_parameters)
    print 'FWHM:', lecture5_lib.fwhm(x, y)
    f.close()
    
    x = [.1, .2, .3, .4, .5]
    y = [0, 1, 2, 2, 1]
    
    print 'hw4a: ', lecture5_lib.peak_position(x, y)
    print 'hw4a: ', lecture5_lib._get_peak_index(y)
    # answer to homework 4a: returns the index of the first value in y that is the maximum

if __name__ == '__main__':
    main()
