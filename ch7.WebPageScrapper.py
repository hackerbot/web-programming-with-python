url = 'http://'+input('Enter a website url: ')

def urlcontent():
    import urllib.request
    with urllib.request.urlopen(url) as response:
       html = response.read()
    print(html)
    content = response.readlines()
    print(content)
#     contents[0]
#      try:
#          if response.getcode() == 200:
#              print('Bingo!')
#          else:
#              print('The response code was not 200, but: {}'.format(
#                      response.getcode()))
#      except urllib.error.HTTPError as e:
#          print('''An error occured: {}
#      The response code was ()'''.format(e, e.getcode()))                   
    print('\n\nHeader:\n\n')
    headerinfo = response.info()
    print(headerinfo)

def urlretrieve():
    import urllib.request
    with urllib.request.urlretrieve(url, filename=urlcontent) as request:
        request.close()

def urlparser():
    import urllib.request, formatter, sys, html
    from html.parser import HTMLParser
    with urllib.request.urlopen(url) as response:
        data = str(response.read())
        response.close()
        format = formatter.AbstractFormatter(formatter.DumbWriter(
            sys.stdout))
        ptext = HTMLParser(format)
        ptext.feed(data)
        ptext.close()

def urlparser2():
    import urllib.request, urllib.parse, formatter
    from html.parser import HTMLParser
    response = urllib.request.urlopen(url)
    data = response.read()
    response.close()
    format = formatter.AbstractFormatter(formatter.NullFormatter())
    ptext = HTMLParser(format)
    ptext.feed(data)
    for link in ptext.anchorlist:
        print(link)


urlcontent()
urlretrieve()
urlparser() # bug in Python 3.5, works in P2.7
urlparser2() # bug in Python 3.5, works in P2.7