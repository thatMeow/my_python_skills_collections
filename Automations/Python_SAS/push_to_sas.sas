# The script below is a SAS script to upload excel file to a SAS data set on the server (sas_table.sas7bdat).
# Use a python script to execute the SAS script



libname out '/prod/user/home/qpc312/IPOD/Automations/Auto_CRM_Input_File_Automation';
 
proc import out=out.sas_table_name
datafile='/prod/user/home/qpc312/IPOD/Automations/Auto_CRM_Input_File_Automation/FB_Volume_2017MA_ - Output.xlsx'

DBMS=XLSX 
REPLACE;
sheet="Sheet1";
 
run;
