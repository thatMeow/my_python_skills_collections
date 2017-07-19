
from ponymail import ponymail

if __name__ == '__main__':

    m = ponymail(
        fromaddr='sender@capitalone.com',
        toaddr='rajkumar.shanmugam@capitalone.com',
        subject='Test Subject',
        body='Hello',
        mailtype='plain'
        )

    m.sendmail()
