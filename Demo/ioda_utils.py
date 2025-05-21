import sys 
from netCDF4 import Dataset
import pandas as pd
import subprocess
import numpy as np

#from ioda_utils import get_meta_data,get_obs_value,get_obs_error,satellite_id_subset,lat_window_subset,get_variable

# ---- (Helper) Functions

def get_meta_data(data):
    MetaData = data.groups['MetaData']
    print(MetaData)
    return(MetaData)

def get_obs_value(data):
    ObsValue = data.groups['ObsValue']
    print(ObsValue)
    return(ObsValue)

def get_obs_error(data):
    ObsError = data.groups['ObsError']
    print(ObsError)
    return(ObsError)

def satellite_id_subset(arr, kx):
    arr_kx = arr[np.isin(arr['satelliteIdentifier'], kx)]
    #print(arr.dtype.names)
    return(arr_kx)

def lat_window_subset(arr, window):
    arr_kx = arr[np.isin(arr['latitude'], window)]
    return(arr_kx)

def get_variable(data,group,name):
    x = data.groups[group].variables[name][:]
    return(x)



 #python3 bufr_to_ioda.py -i obsdatain -o obsdataout -y yaml_template
if __name__ == "__main__":   
    # data
    #testfile = Dataset('wrkdir/function-outputs/iodadir/GPSRO_final/Y2022/M01/gdas1_spnasa.220101.t00z.gpsro.tm00.ioda.nc4', mode ='r')
    #ioda_file = Dataset('gdas1_spnasa.220101.t18z.gpsro.tm00.ioda.nc4', mode ='r')
    #latitude = get_variable(ioda_file,'MetaData','latitude')

    #data = sys.argv[1]
    ioda_file = Dataset(sys.argv[1], mode ='r')


    meta = get_meta_data(ioda_file)
    #help(get_meta_data)

    attribute_names = ioda_file.ncattrs()
    print(attribute_names)

    for attr_name in ioda_file.ncattrs():
        attr_value = ioda_file.getncattr(attr_name)
        print(f"{attr_name}: {attr_value}")