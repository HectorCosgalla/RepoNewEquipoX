from bs4 import BeautifulSoup
import urllib2
#import publicaciones

facebookFile = urllib2.urlopen("https://www.facebook.com/pg/lacreperieremerida/posts/?ref=page_internal")
facebookHtml = facebookFile.read()
facebookFile.close()

soup = BeautifulSoup(facebookHtml)
  
cadena = str(soup.find_all("p"))

print(cadena)

anterior = 0
urlPublic = []
for i in range(25):
	busquedaURl = cadena.find("<p>",anterior+3)
	if (busquedaURl > 0):
    		urlPublic.append(cadena[busquedaURl:busquedaURl+100])
    		anterior = busquedaURl

for i in urlPublic:
	break
	#print(i)
	#publicaciones.public(i)