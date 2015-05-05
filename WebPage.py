def urlopen():
    import urllib.request
    url = 'http://'+input('Enter a website url: ')
    with urllib.request.urlopen(url) as response:
       html = response.read()
    print(html)
    contents = response.readlines()
    print(contents)
    #contents[0]
    headerinfo = response.info()
    print(headerinfo)

#urlopen()

def urlparser():
    import urllib.request, formatter, sys, html
    from html.parser import HTMLParser
    url = 'http://'+input('Enter a website url: ')
    with urllib.request.urlopen(url) as response:
        data = str(response.read())
        response.close()
        format = formatter.AbstractFormatter(formatter.DumbWriter(sys.stdout))
        ptext = HTMLParser()
        ptext.feed(data)
        ptext.close()

urlparser() #bug in Python 3.5, works in P2.7

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
    def handle_data(self, data):
        print("Encountered some data  :", data)

#url = 'http://'+input('Enter a website url: ')
#parser = MyHTMLParser()
#parser.feed(url)