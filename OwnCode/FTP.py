#ftp 'ftp.url.com'
#dir
#put filename

filename = input('Enter filename:\n')

def getdir():
    import ftplib
    connect = ftplib.FTP('ftp.url.com')
    connect.login('administrator\admin', 'password')
    data = []
    connect.dir(data.append)
    connect.quit()
    for line in data:
        print(line)

def getfile():
    import ftplib
    import sys
    filename = sys.argv[1]
    connect = ftplib.FTP('ftp.url.com')
    connect.login('administrator\admin', 'password')
    connect.retrlines('RETR ' + filename)
    connect.quit()

def putfile():
    import ftplib
    import sys
    connect = ftplib.FTP('ftp.url.com')
    connect.login('administrator\admin', 'password')
    file = open(filename, 'rb')
    connect.storebinary('STOR ' + filename, file)
    connect.quit()    