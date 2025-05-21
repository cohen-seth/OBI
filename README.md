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

# Pre-Installation
Suggest that you first locate the following and copy their respective paths to a txt file or anywhere you can easily access it for copy and paste later on:
1. The script you use to load JEDI and/or Swell if you have one. If you don't have one disregard this - you will create one during the installation process.
2. Paths to the files you wish to convert - you will need this for copying the data files into the `OBI/Demo/data/` folder.
3. Path to your `jedi_bundle/build/bin` - if you have a `Swell Experiments` folder you may be able to use the path `{Swell Experiments}/

# Installation and Environment Setup


In order to run the Ioda Converter, `bufr2ioda.x`, you will need  


1. Clone the gmao-utils repo.
```sh
$ git clone https://github.com/cohen-seth/gmao-utils.git
```

2. Next, open and edit config file:
```sh
$
$
```
2. Load Jedi - either directly or through Swell
3. Find your /build/bin/bufr2ioda.x 
4. Add `bufr2ioda.x` to PATH
5. You will need to copy the data files you want to convert into the Demo/data/ directory

# Function examples

bufr2ioda.x
## 1. Locate the 
```sh
$ bufr2ioda.x [PATH OF YAML TEMPLATE]
```


bufr2ioda_offline_driver.py
```sh
$ python3 bufr2ioda_offline_driver.py [PATH TO BUFR FILE(S)] [PATH OF IODA FILE(S)] [PATH OF YAML TEMPLATE]
```

5. *OPTIONAL* Then, you may want to inspect and verify LoadJedi.sh. You should NOT need to edit this file; HOWEVER, you may need to in the future if there is a more recent build of JEDI/IODA. The everything in this file must point to a current build of the JEDI IODA CONVERTERS.
