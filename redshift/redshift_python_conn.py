import psycopg2  
import getpass  
import sys  
from os.path import expanduser  
  
  
def redshift_connect():  
    try:  
        l_user = getpass.getuser()  
        home = expanduser("~")  
        f = open(home + '/.tdlogon')  
        logline = f.readline()  
        usr = logline.split(',')[0].split('/')[1].strip()  
        pwd = logline.split(',')[1].rstrip()  
  
  
        conn_redshift=psycopg2.connect(dbname= 'db', host='pbcdwp.cloud.capitalone.com',  
        port= 5439, user= usr, password= pwd)  
        return conn_redshift  
    except IOError as e:  
        print 'I/O error ({0}): {1}: .tdlogon missing!!'.format(e.errno, e.strerror)  
    except:  
        print 'Warning: Unexpected Error:',sys.exc_info()[0]  
    raise 
