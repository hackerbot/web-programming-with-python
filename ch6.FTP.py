# ftp 'ftp.url.com'
# dir
# put filename

filename = input('Enter filename: ')

def getdir():
    import ftplib
    url = 'ftp://'+input('Enter FTP url: ')
    connect = ftplib.FTP(url)
    username = input('Enter username: ')
    password = input('Enter password: ')
    connect.login(username, password)
    data = []
    connect.dir(data.append)
    connect.quit()
    for line in data:
        print(line)

def getfile():
    import ftplib
    import sys
    filename = sys.argv[1]
    url = 'ftp://'+input('Enter FTP url: ')
    connect = ftplib.FTP(url)
    username = input('Enter username: ')
    password = input('Enter password: ')
    connect.login(username, password)
    connect.retrlines('RETR ' + filename)
    connect.quit()

def putfile():
    import ftplib
    import sys
    url = 'ftp://'+input('Enter FTP url: ')
    connect = ftplib.FTP(url)
    username = input('Enter username: ')
    password = input('Enter password: ')
    connect.login(username, password)
    file = open(filename, 'rb')
    connect.storebinary('STOR ' + filename, file)
    connect.quit()    