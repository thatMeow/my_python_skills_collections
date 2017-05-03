
libname out 'path';

proc import out=out.sas_output_dataset
datafile='path/sample_excel.xlsx'

DBMS=XLSX 
REPLACE;

sheet="Sheet1";

run;

data out.sas_output_dataset(rename=(vintage2=vintage)); /* vintage is the column that needs to be formatted. vintage2 is a 
temporary column*/
format vintage2 date9.; /*date9. is the format DDMMMYYYY. e.g.01JAN2000*/

set out.sas_output_dataset;

vintage2 = vintage-21916; /* minus the data to get correct data. since excel data starts at 1900/01/01 and sas starts at 1960/01/01*/
drop vintage;

run;
