from nntplib import *

def readnews():
    url = 'nttp://'+input('Enter Newsgroup url: ') # e.g. web.aioe.org
    s = NNTP(url) # www.elfqrin.com/hacklab/pages/nntpserv.php
    (resp, count, first, last, name) = s.group('comp.lang.python')
    (resp, subs) = s.xhdr('subject', (str(first)+'-'+str(last)))
    for subject in subs[-10:]:
        print(subject)
    number = input('Which article do you want to read?\n')
    (reply, num, id, list) = s.body(str(number))
    for line in list:
        print(line)
        
readnews()