
prepbufr conversion tests


# FAILED WHEN USING THE BUFR2IODA.X LOADED FROM SWELL !!!!
####################################################################
python3 bufr2ioda_offline_driver.py data/prepbufr/gdas1.201201.t00z.prepbufr ./data/prepbufr/gdas1.200101.t00z.bufr_ncep_rtma_prepbufr_adpupa.nc4 data/prepbufr/bufr_ncep_rtma_prepbufr_adpupa.yaml ~ bufr2ioda.x: symbol lookup error:
python3 bufr2ioda_offline_driver.py data/prepbufr/gdas1.201201.t00z.prepbufr ./data/prepbufr/gdas1.200101.t00z.bufr_ncep_prepbufr_adpsfc.nc4 data/prepbufr/bufr_ncep_prepbufr_adpsfc.yaml ~ bufr2ioda.x: symbol lookup error:
python3 bufr2ioda_offline_driver.py data/prepbufr/gdas1.201201.t00z.prepbufr ./data/prepbufr/gdas1.200101.t00z.bufr_ncep_prepbufr_aircft.nc4 data/prepbufr/bufr_ncep_prepbufr_aircft.yaml
python3 bufr2ioda_offline_driver.py data/prepbufr/gdas1.201201.t00z.prepbufr ./data/prepbufr/gdas1.200101.t00z.bufr_ncep_prepbufr_adpupa.nc4 data/prepbufr/bufr_ncep_prepbufr_adpupa.yaml
python3 bufr2ioda_offline_driver.py data/prepbufr/gdas1.201201.t00z.prepbufr ./data/prepbufr/gdas1.200101.t00z.bufr_ncep_rtma_prepbufr_adpupa.nc4 data/prepbufr/bufr_ncep_rtma_prepbufr_adpupa.yaml
####################################################################

# JediWork/load_jedi.csh
FAILED:
#######
python3 bufr2ioda_offline_driver.py data/prepbufr/gdas1.201201.t00z.prepbufr ./data/prepbufr/gdas1.200101.t00z.bufr_ncep_rtma_prepbufr_adpupa.nc4 data/prepbufr/bufr_ncep_rtma_prepbufr_adpupa.yaml 
python3 bufr2ioda_offline_driver.py data/prepbufr/gdas1.201201.t00z.prepbufr ./data/prepbufr/gdas1.200101.t00z.bufr_ncep_prepbufr_adpupa.nc4 data/prepbufr/bufr_ncep_prepbufr_adpupa.yaml

COULDNT FIND SOME BUT SUCCESSFUL:
#################################
python3 bufr2ioda_offline_driver.py data/prepbufr/gdas1.201201.t00z.prepbufr ./data/prepbufr/gdas1.200101.t00z.bufr_ncep_prepbufr_adpsfc.nc4 data/prepbufr/bufr_ncep_prepbufr_adpsfc.yaml
python3 bufr2ioda_offline_driver.py data/prepbufr/gdas1.201201.t00z.prepbufr ./data/prepbufr/gdas1.200101.t00z.bufr_ncep_prepbufr_aircft.nc4 data/prepbufr/bufr_ncep_prepbufr_aircft.yaml
python3 bufr2ioda_offline_driver.py data/prepbufr/gdas1.201201.t00z.prepbufr ./data/prepbufr/gdas1.200101.t00z.bufr_ncep_prepbufr_aircft.nc4 data/prepbufr/bufr_ncep_prepbufr_adpsfc_cloud_rrfs.yaml
"""
