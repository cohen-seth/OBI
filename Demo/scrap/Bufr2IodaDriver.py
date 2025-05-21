import logging
import os
import yaml
from datetime import datetime, timedelta
import subprocess
import glob
from pathlib import Path
from ruamel.yaml.scalarstring import SingleQuotedScalarString, DoubleQuotedScalarString
import argparse

#################################
class Bufr2IodaBase:
    def __init__(self, config_yaml_path): 
        """
        Initialize the PyRadmonBase class using a YAML configuration file.
        :param config_yaml_path: Path to the YAML configuration file. See PyRadmonBase_template.yaml
        
        """

        with open(config_yaml_path, 'r') as file:
            config = yaml.safe_load(file)
            #print(f'config: {config}')
        
                #################################
        self.obsdatain = config['obsdatain'] #e5303_m21c_jan18
        self.obsdataout = config['obsdataout'] # 20190530 000000
        self.yaml_template = config['yaml_template'] # 20190531 180000

        def create_iodaconv_yaml(self.obsdatain,self.obsdataout,self.yaml_template,output_yaml=None):
        #def create_iodaconv_yaml(self):
            """
            Creates the YAML file need to convert a BUFR file to IODA.
            Uses an existing file for the appropriate obs type as a template; the values for self.obsdatain & self.obsdataout are updated in the new yaml file based on the user input.
            
            self.obsdatain is the path used to find the BUFR file that you want to convert.
            self.obsdataout is the path/filename for the resulting converted IODA file. 

            
            self.obsdatain:path
            self.obsdataout:path
            self.yaml_template:path ; yaml file to use to replicate the structure for the specific obs_type
            output_yaml:str

            # Test/Example
            create_iodaconv_yaml(
                self.obsdatain = "./AMSUA/Y2021/M11/gdas1.211101.t00z.1bamua.tm00.bufr_d",
                self.obsdataout = "./ioda/gdas1.211101.t00z.1bamua.tm00.nc4" ,
                self.yaml_template='/Users/sicohen/Documents/GitHub/swell/bufr_amsua.yaml',
                output_yaml=None)
            """
            print(f"Inputs given: \n self.obsdatain:{self.obsdatain} \n self.obsdataout:{self.obsdataout} \n self.yaml_template:{self.yaml_template} \n")

            output_yaml=None
            self.obsdatain = str(self.obsdatain)
            self.obsdataout = str(self.obsdataout)
            self.yaml_template = str(self.yaml_template)
            
            try:
                    # Load the YAML template file 
                    with open(str(self.yaml_template), 'r') as file:
                        yaml_content = yaml.safe_load(file)
            
                    # Apply the replacements
                    yaml_content['observations'][0]['obs space']['obsdatain'] = self.obsdatain #DoubleQuotedScalarString(self.obsdatain) #str(self.obsdatain) # input bufr file path.
                    yaml_content['observations'][0]['ioda']['obsdataout'] = self.obsdataout #DoubleQuotedScalarString(self.obsdataout) #str(self.obsdataout) # output path and/or filename for the converted ioda file.
                    
                    print("self.obsdatain:", self.obsdatain)
                    print("self.obsdataout:", self.obsdataout)
            
                    # Determine the output file path
                    if output_yaml is None:
                        output_yaml = "updated_iodaconv.yaml"  # Overwrite original if no output file is specified
                        
                    # Determine the yaml template file path
                    #if self.yaml_template is None:
                    #    self.yaml_template = "updated_iodaconv.yaml"  # Overwrite original if no output file is specified
                    #if obs_type == 'amsua' ... then ... set yaml path to predefined path...
                
                    # Write the updated data to the specified output file
                    with open(output_yaml, 'w') as file:
                        yaml.dump(yaml_content, file, default_flow_style=False, sort_keys=False)
                        print("Updated YAML file content:")
                        #print(yaml.dump(yaml_content, default_flow_style=False, sort_keys=False))        
                    
                    print(f"YAML file saved as '{output_yaml}'.")
            
            except FileNotFoundError:
                print(f"Error: File '{self.yaml_template}' not found.")
            except yaml.YAMLError as e:
                print(f"Error processing YAML file: {e}")
            return output_yaml


        # 2) find_file will be get_bufr.py ... maybe?
        # File/Directory parser
        def find_file(file_pattern, search_dir="."):
            """
            Search for a file in the given directory and subdirectories.
            :param file_pattern: Pattern of the file to search for (e.g., '*.txt' or 'file.txt')
            :param search_dir: Directory to search in (default is current directory)
            :return: List of found file paths
            """
            search_path = os.path.join(search_dir, "**", file_pattern)
            files = glob.glob(search_path, recursive=True)
            return files

        # Subprocess wrapper ~ call the ioda converter and run (bufr2ioda.x)
        def run_conversion(yaml_file_path, executable_path=None):
            """
            Run an executable on the given file.
            :param executable_path: Path to the executable
            :param file_path: Path to the file to process
            :return: None
            """
            if executable_path is None:
                executable_path = 'bufr2ioda.x'    
            try:
                subprocess.run([executable_path, yaml_file_path], check=True)
                print(f"Successfully ran {executable_path} on {yaml_file_path}")
            except subprocess.CalledProcessError as e:
                print(f"Error running {executable_path}: {e}")
            except FileNotFoundError:
                print(f"Executable not found: {executable_path}")


# python script.py config.yaml
if __name__ == "__main__":

    print(os.path.basename(__file__))
    parser = argparse.ArgumentParser(description="configuration YAML file.")
    #parser = argparse.ArgumentParser(description="python3 bufr_to_ioda.py -i obsdatain -o obsdataout -y yaml_template")
    parser.add_argument("config", help="Path to the YAML configuration file.")
    args = parser.parse_args()

    A = Bufr2Ioda(args.config)
    #yaml_file_path = A.create_iodaconv_yaml()
    #A.run_conversion(yaml_file_path)
