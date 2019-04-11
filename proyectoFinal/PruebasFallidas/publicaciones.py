from bs4 import BeautifulSoup
import urllib2

def public(urlPublic):

	facebookFile = urllib2.urlopen(urlPublic)
	facebookHtml = facebookFile.read()
	facebookFile.close()

	soup = BeautifulSoup(facebookHtml)
  
	cadena = str(soup.find_all('body'))
	if(cadena.find("<p>") > 0):
		print(cadena[cadena.find("<p>")+3:cadena.find("</p>")])
		print(cadena[cadena.find('data-pl')+11:cadena.find('data-pl')+12])

