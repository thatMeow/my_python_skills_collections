import glob
import os

curr_path=os.getcwd()
os.chdir(curr_path)

files = [f for f in os.listdir('.') if not os.path.isdir(f)]
recentExc = [f for f in files if f[-5:] == '.xlsx']
recentExc.sort(key = lambda f: os.path.getctime(f))

input_excel_file = recentExc[-1] # most recent file

# If PDF file:
recentPDFs = [f for f in files if f[-4:] == '.pdf'] # Checks the file extension is pdf
recentPDFs.sort(key = lambda f: os.path.getmtime(f), reverse = True)

input_excel_file = recentExc[-1]
