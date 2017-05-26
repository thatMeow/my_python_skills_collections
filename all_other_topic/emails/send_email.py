from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import smtplib

class send_email(object):

    def __init__(self, fromaddr, toaddr, subject, body, mailtype='plain', cc=None, bcc=None):
        self.fromaddr = fromaddr
        self.toaddr = toaddr
        self.subject = subject
        self.body = body
        self.cc = cc if cc is not None else list()
        self.bcc = bcc if bcc is not None else list()
        self.attachment = list()
        self.server = smtplib.SMTP(server name here)
        self.mailtype = mailtype

    def sendmail(self):
        if isinstance(self.toaddr, str):
            self.toaddr = [self.toaddr]
        if isinstance(self.cc, str):
            self.cc = [self.cc]
        if isinstance(self.bcc, str):
            self.bcc = [self.bcc]
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['Subject'] = self.subject
        msg['To'] = ','.join(self.toaddr)
        msg['Cc'] = ','.join(self.cc)
        msg['Bcc'] = ','.join(self.bcc)
        toaddrs = self.toaddr + self.cc + self.bcc
        msg.attach(MIMEText(self.body, self.mailtype))
        for a in self.attachment:
            msg.attach(a)
        self.server.sendmail(self.fromaddr, toaddrs, msg.as_string())
        self.server.quit()

    def add_attachment(self, file):
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(file, 'rb').read())
        encoders.encode_base64(part)
        filename = file.split('/')[-1]
        part.add_header("Content-Disposition", "attachment; filename={}".format(filename))
        self.attachment.append(part)
