# This Python script execute the sas script. "sas_file_name_path_and_file_name" is the actual sas file that execute the sas process.
# In this case the "sas_file_name_path_and_file_name" should be "push_to_sas.sas"


import subprocess

# execute the sas script and upload excel file to server
subprocess.call(["sasgsub", "-gridsubmitpgm", sas_file_name_path_and_file_name])



