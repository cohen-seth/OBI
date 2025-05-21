import os
import subprocess
import glob
import yaml
from pathlib import Path
from ruamel.yaml.scalarstring import SingleQuotedScalarString, DoubleQuotedScalarString

# 1) 
def create_iodaconv_yaml(obsdatain,obsdataout,yaml_template,output_yaml=None):
    """
    Creates the YAML file need to convert a BUFR file to IODA.
    Uses an existing file for the appropriate obs type as a template; the values for obsdatain & obsdataout are updated in the new yaml file based on the user input.
    
    obsdatain is the path used to find the BUFR file that you want to convert.
    obsdataout is the path/filename for the resulting converted IODA file. 

    
    obsdatain:path
    obsdataout:path
    yaml_template:path ; yaml file to use to replicate the structure for the specific obs_type
    output_yaml:str

    # Test/Example
    create_iodaconv_yaml(
        obsdatain = "./AMSUA/Y2021/M11/gdas1.211101.t00z.1bamua.tm00.bufr_d",
        obsdataout = "./ioda/gdas1.211101.t00z.1bamua.tm00.nc4" ,
        yaml_template='/Users/sicohen/Documents/GitHub/swell/bufr_amsua.yaml',
        output_yaml=None)
    """

    #yaml.preserve_quotes = True
    yaml_template = "/discover/nobackup/sicohen/Ricardo/test-iodaconv/swell-suite/offline/bufr_amsua.yaml"
    try:
            # Check if the file exists
            if not os.path.isfile(yaml_template):
                print(f"Error: File '{yaml_template}' does not exist.")
                return  # Stop the function if the file is not found

            # Load the YAML template file 
            with open(yaml_template, 'r') as file:
                yaml_content = yaml.safe_load(file)
    
            # Apply the replacements
            #yaml_content['observations'][0]['obs space']['obsdatain'] = DoubleQuotedScalarString(obsdatain) # input bufr file path.
            #yaml_content['observations'][0]['ioda']['obsdataout'] = DoubleQuotedScalarString(obsdataout) # output path and/or filename for the converted ioda file.
            # Apply the replacements
            yaml_content['observations'][0]['obs space']['obsdatain'] = "/discover/nobackup/projects/gmao/input/dao_ops/obs/flk/ncep_g5obs/bufr/AMSUA/Y2021/M11/gdas1.211101.t00z.1bamua.tm00.bufr_d" # input bufr file path.
            yaml_content['observations'][0]['ioda']['obsdataout'] = "./gdas1.211101.t00z.1bamua.tm00.nc4" # output path and/or filename for the converted ioda file.
            
            print("obsdatain:", obsdatain)
            print("obsdataout:", obsdataout)
    
            # Determine the output file path
            if output_yaml is None:
                output_yaml = "updated_iodaconv.yaml"  # Overwrite original if no output file is specified
                
            # Determine the yaml template file path
            #if yaml_template is None:
            #    yaml_template = "updated_iodaconv.yaml"  # Overwrite original if no output file is specified
            #if obs_type == 'amsua' ... then ... set yaml path to predefined path...
        
            # Write the updated data to the specified output file
            with open(output_yaml, 'w') as file:
                yaml.dump(yaml_content, file, default_flow_style=False, sort_keys=False)
                print("Updated YAML file content:")
                print(yaml.dump(yaml_content, default_flow_style=False, sort_keys=False))        
            
            print(f"YAML file saved as '{output_yaml}'.")
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
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

def main():
    # Example usage
    #search_dir = input("Enter the directory to search: ")
    #file_pattern = input("Enter the file pattern (e.g., '*.txt'): ")
    #executable_path = input("Enter the path to the executable: ")
    #obsdatain = input("Enter the path of the BUFR file you wish to convert (e.g. obsdatain; *.bufr_d):")
    #obsdataout = input("Enter the path/filename you wish to save the converted IODA file as (e.g. obsdataout; *.nc4):")
    #yaml_template = input("Enter the path to the YAML file to use as a template for generating the yaml file for the bufr2ioda.x conversion:")
    
    # Find the file
    #files = find_file(file_pattern, search_dir)
    
    # Make the yaml file
    obsdatain = "/discover/nobackup/projects/gmao/input/dao_ops/obs/flk/ncep_g5obs/bufr/AMSUA/Y2021/M11/gdas1.211101.t00z.1bamua.tm00.bufr_d"
    obsdataout = "./gdas1.211101.t00z.1bamua.tm00.nc4"
    yaml_template = "/discover/nobackup/sicohen/Ricardo/test-iodaconv/swell-suite/offline/bufr_amsua.yaml"
 
    yaml_file_path = create_iodaconv_yaml(obsdatain,obsdataout,yaml_template,output_yaml=None)

    if not yaml_file_path:
        print("No files found matching the pattern.")
        return

    # Run the executable on each found file
    run_conversion(yaml_file_path)

if __name__ == "__main__":
    main()

