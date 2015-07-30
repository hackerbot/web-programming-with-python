# url = 'http://'+input('Enter a website url: ')
url = 'http://finance.google.com/finance?g='

def ScreenScrapper():
	import urllib.request, re# , sys
	
	symbol = input('Enter a company symbol: ')
	# symbol = sys.argv[1]
	content = urllib.request.urlopen(url+symbol).read()
	m = re.search('span id="ref.*>(.*)<', content)
	if m:
		quote = m.group(1)
	else:
		quote = 'no quote for symbol: ' + symbol
	print(quote)

def WebScrapper():
	import urllib.request, formatter, re# , sys
	from html.parser import HTMLParser
	
	response = urllib.request.urlopen(url)
	data = response.read()
	response.close()
	format = formatter.AbstractFormatter(formatter.NullWriter())
	ptext = HTMLParser(format)
	ptext.feed(data)
	links = []
	links = ptext.anchorlist
	for link in links:
		if re.search('http', link) !=None:
			print(link)
			website = urllib.request.urlopen(link)
			data = response.read()
			response.close()
			ptext = HTMLParser(format)
			ptext.feed(data)
			morelinks = ptext.anchorlist
			for alink in morelinks:
				if re.search('http', alink) !=None:
					links.append(alink)

# ScreenScrapper()
WebScrapper()