import pandas as pd
import numpy as np
import h5py as h5


for i in range(0, 11):
#In this case, a total of 10 slices are retrieved from the digital model in Rhino through the Grasshopper script.
    df = pd.read_csv(r'\gh_output\%s.csv'%i)
    t = np.array(df).astype(int)
    t = np.squeeze(t)
    t = np.append(t, 0)
    t = t.reshape((243, 1, 200))
    t = np.transpose(t, (2, 1, 0))
    t = np.flip(t, axis = 2)

    new = h5.File(r'\gh_output\%i.h5'%i, 'w')
    new.attrs['dx_dy_dz'] = [0.01, 0.01, 0.01]
    new['data'] = t
    new.close()
