from bs4 import BeautifulSoup
import urllib2

facebookFile = urllib2.urlopen("https://www.facebook.com/groups/870931949699072/permalink/1947088962083360/")
facebookHtml = facebookFile.read()
facebookFile.close()

soup = BeautifulSoup(facebookHtml)
  
cadena = str(soup.find_all('body'))

if(cadena.find("<p>") > 0):
	print(cadena[cadena.find("<p>"):cadena.find("</p>")])
	print(cadena[cadena.find('data-pl')+11:cadena.find('data-pl')+211])

