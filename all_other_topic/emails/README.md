# Ponymail

## Description

Python module to send emails through Capital One's SMTP Server.

Capital One SMTP Server is **_ponyex.capitalone.com_**. This SMTP server will only accept connections from allowed servers. As a result, you won't be able to send messages from your laptop.

## Installation
```unix
git clone git@github.kdc.capitalone.com:fiq831/ponymail.git
cd ponymail
python setup.py install --user
```

## Using Ponymail

Send a simple text message. The default MIME type is text/plain. 

```python
# fromaddr == the sender's email address
# toaddr == the recipient's email address
m = ponymail(fromaddr = 'sender@capitalone.com',
             toaddr = 'receiver@capitalone.com',
             subject = 'Subject Line',
             body = 'Message',
             mailtype = 'plain',  # optional
             cc = 'user1@capitalone.com', # optional
             bcc = 'user2@capitalone.com') # optional
m.sendmail()
```

Send a message with CC and BCC.
```python
m = ponymail(fromaddr = 'sender@capitalone.com',
             toaddr = 'receiver@capitalone.com',
             subject = 'Subject Line',
             body = 'Message',
             cc = 'user1@capitalone.com',
             bcc = 'user2@capitalone.com')
m.sendmail()
```

Send a message to multiple users.
```python
# toaddr == pass a list of users
m = ponymail(fromaddr = 'sender@capitalone.com',
             toaddr = ['user1@capitalone.com','user2@capitalone.com'],
             subject = 'Subject Line',
             body = 'Message',
             cc = ['user3@capitalone.com','user4@capitalone.com'],
             bcc = ['user5@capitalone.com','user6@capitalone.com'])
m.sendmail()
```

Send an HTML message.
```python
html_content = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="https://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""
m = ponymail(fromaddr = 'sender@capitalone.com',
             toaddr = 'receiver@capitalone.com',
             subject = 'Subject Line',
             body = html_content,
             mailtype = 'html')
m.sendmail()
```

Send a message with attachment.
```python
m = ponymail(fromaddr = 'sender@capitalone.com',
             toaddr = 'receiver@capitalone.com',
             subject = 'Subject Line',
             body = 'Message')
m.add_attachment('/path/to/file')
m.sendmail()
```
