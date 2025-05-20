# Offline BUFR to IODA Converter

# Dependencies:

Colons can be used to align columns.

| Dependencies  |               |       |
| ------------- |:-------------:| -----:|
| JEDI          |               |       |
| IODACONV      |               |       |
| bufr2ioda.x   |               |       |
| yaml_template |               |       |


---






# gmao-utils
NASA/GMAO. Tools for working with  data files in both BUFR and IODA (JEDI) format.

# Directory Structure (skeleton)

# Installation and Environment Setup

1. Clone the gmao-utils repo.
```sh
$ git clone https://github.com/cohen-seth/gmao-utils.git
```

2. Next, open and edit config_gmao_utils.sh *ONLY!* :
```sh
$ cd gmao-utils
$ vim config_gmao_utils.sh
```
2. Load Jedi
3. Demo

# Function examples

convert_bufr2ioda.py
```sh
$ python src/gpsro_utils/convert_bufr2ioda.py [PATH TO BUFR FILE(S)] [PATH OF IODA FILE(S)] [PATH OF YAML TEMPLATE]
```

5. *OPTIONAL* Then, you may want to inspect and verify LoadJedi.sh. You should NOT need to edit this file; HOWEVER, you may need to in the future if there is a more recent build of JEDI/IODA. The everything in this file must point to a current build of the JEDI IODA CONVERTERS.
