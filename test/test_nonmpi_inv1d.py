import numpy as np
import hazel
import h5py
import os

def test_nonmpi_inv1d():
# Test iterator with a single observation in synthesis
    iterator = hazel.Iterator(use_mpi=False)
    rank = iterator.get_rank()
    mod = hazel.Model('test/configurations/conf_nonmpi_inv1d.ini', working_mode='inversion', verbose=2, randomization=2)
    iterator.use_model(model=mod)
    iterator.run_all_pixels()

    if (rank == 0):
        
        f = h5py.File('output.h5', 'r')

        assert f['spec1']['stokes'].shape == (1,2,1,4,150), "incorrect dimensions in inversion"

        f.close()

        try:
            os.remove('output.h5')
        except:
            pass