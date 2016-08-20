'''
Python code used in APS 2016 Python lecture 5
'''

import h5py
import lecture5_lib

f = h5py.File('writer_1_3.hdf5', 'r')
x = f['/Scan/data/two_theta']
y = f['/Scan/data/counts']
print 'file:', f.filename
print 'peak position:', lecture5_lib.peak_position(x, y)
print 'center-of-mass:', lecture5_lib.center_of_mass(x, y)
print 'FWHM:', lecture5_lib.fwhm(x, y)
f.close()

x = [.1, .2, .3, .4, .5]
y = [0, 1, 2, 2, 1]

print 'hw4a: ', lecture5_lib.peak_position(x, y)
print 'hw4a: ', lecture5_lib._get_peak_index(y)
# answer to homework 4a: returns the index of the first value in y that is the maximum

def dummy():
  ''' '''
