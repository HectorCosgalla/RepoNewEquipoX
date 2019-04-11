from bs4 import BeautifulSoup
import urllib2
import os

def urlText(urlPage):
	urlBase = urlPage
	facebookFile = urllib2.urlopen(urlBase)
	facebookHtml = facebookFile.read()
	facebookFile.close()

	soup = BeautifulSoup(facebookHtml)

	file = open('publicaciones.csv','w')

	for string in soup.find_all('p'):
		file.write(repr(string))
		file.write(os.linesep)

	file.close()    
