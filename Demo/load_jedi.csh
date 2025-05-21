#!/usr/local/bin/csh

#------------------------
# Load JEDI spack Python module
#------------------------
module purge
#source /discover/nobackup/projects/gmao/advda/swell/jedi_modules/bundle-intel-sles15
module use -a /discover/nobackup/projects/gmao/advda/JediOpt/modulefiles/core/
module load jedi_bundle/sles15_skylab7
#source $NOBACKUP/JediWork/latest/build-intel-release/modules
source /discover/nobackup/projects/gmao/advda/swell/JediBundles/fv3_soca_SLES15/build-intel-release/modules
#------------------------
# Load JEDI
#------------------------
setenv jedibuild $NOBACKUP/JediWork/latest/build-intel-release
setenv jedisrc $NOBACKUP/JediWork/latest
setenv PATH $jedibuild/bin:$PATH
#------------------------
# Ioda Python
#------------------------
setenv LD_LIBRARY_PATH $jedibuild/lib:$LD_LIBRARY_PATH
setenv PYTHONPATH $jedibuild/lib/python3.10/:$PYTHONPATH
setenv PYTHONPATH $jedibuild/lib/python3.10/pyioda:$PYTHONPATH
setenv PYTHONPATH $jedibuild/lib/pyiodaconv:$PYTHONPATH
setenv PYTHONPATH $jedibuild/iodaconv/src:$PYTHONPATH

#module swap stack-intel stack-gcc/10.1.0
