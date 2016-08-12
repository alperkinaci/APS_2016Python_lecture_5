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

def dummy():
  ''' '''
