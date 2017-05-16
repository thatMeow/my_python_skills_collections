# http://stackoverflow.com/questions/44006814/python-automatically-writing-all-print-statements-to-a-log-fil/44007027#44007027

import sys
sys.stdout = open('log.txt', 'r')

import pandas

print "pandas library imported"
df = pd.Dataframe(...)
print "df created."
