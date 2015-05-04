def reademail():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    import imaplib
    mailserver = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    username = input('Enter your username:\n')
    password = input('Enter your password:\n')
    mailserver.login(username,password)
    status, count = mailserver.select('Inbox')
    status, data = mailserver.fetch(count[0], '(UID BODY[Text])')
    print(data[0][1])
    mailserver.close()
    mailserver.logout()
    choice = input('Press x to clear screen:\n')
    if choice == 'x':
        os.system('cls' if os.name == 'nt' else 'clear')

def sendemail():
    import os
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    fromaddr = input('Enter your email address:\n')
    toaddr = input('Enter the receiver\'s email address:\n')
    subject = input('Enter the subject:\n')
    text = input('Enter the message:\n')
    input('Is your username same as your email?\n')
    if str(input) == 'Y' or 'YES' or 'yes' or 'y' or '1':
        username = fromaddr
    else:
        username = input('Enter your username:\n')
    password = input('Enter your password:\n')
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Test Python'
    msg.attach(MIMEText(text))
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.ehlo()
    server.login(username,password)
    server.sendmail(fromaddr, toaddr, msg.as_string())
    server.quit()
    choice = input('Email sent. Press x to clear the screen:\n')
    if choice == 'x':
        os.system('cls' if os.name == 'nt' else 'clear')

while 1:
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Email Program\n')
    print('1. Read email')
    print('2. Send email')
    print('3. Exit\n')
    choice = input('Enter a choice:\n')
    if choice == '1':
        reademail()
    elif choice == '2':
        sendemail()
    elif choice == '3':
        break