import sys
sys.stdout = open('log.txt', 'r')

import pandas

print "pandas library imported"
df = pd.Dataframe(...)
print "df created."
