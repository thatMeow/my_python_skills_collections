libname out '/prod/user/home/qpc312/IPOD/Automations/Auto_CRM_Input_File_Automation';
 
proc import out=out.fb_volume
datafile='/prod/user/home/qpc312/IPOD/Automations/Auto_CRM_Input_File_Automation/FB_Volume_2017MA_ - Output.xlsx'

DBMS=XLSX 
REPLACE;
sheet="Sheet1";
 
run;
