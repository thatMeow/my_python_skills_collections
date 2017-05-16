# http://stackoverflow.com/questions/44006814/python-automatically-writing-all-print-statements-to-a-log-fil/44007027?noredirect=1#comment75046253_44007027

# This code only saves print messages to a log file, the command line will not have the messages printed out
import sys
sys.stdout = open('log.txt', 'r')

import pandas

print "pandas library imported"
df = pd.Dataframe(...)
print "df created."

# the following code will write messages to command line and save print messages to a file

class Tee(object):
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)

f = open('logfile', 'w')
backup = sys.stdout
sys.stdout = Tee(sys.stdout, f)

print "hello world"  # this should appear in stdout and in file
