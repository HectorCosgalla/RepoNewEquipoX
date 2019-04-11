from bs4 import BeautifulSoup
import urllib2
# import os
import csv

def urlImages(urlPage):

	urlBase = urlPage
	facebookFile = urllib2.urlopen(urlBase)
	facebookHtml = facebookFile.read()
	facebookFile.close()

	soup = BeautifulSoup(facebookHtml)
	file = open('UrlImages.csv','w')
	findUrls(soup,file)
	file.close()
	  
def findUrls(soup,file):
	#file = open('UrlImages.csv','w',newline='')

	for string in soup.find_all('a'):

		cadena  = str(string)
		findUrl = cadena.find('href="/')
		findData = cadena.find('data-ploi')
		findVideo = cadena.find('photos')
		

		if(findUrl > 0 and len(cadena) > 400 and findVideo > 0):
			urls = []
			if(cadena[findUrl+161] == '"' or cadena[findUrl+155] != '"'):
				urlBase = findUrl+6
				count = 0
				for i in range(urlBase,len(cadena)):
					if(cadena[i] == '"' and count < 1):
						finUrl  = i
						count = 2
		
				urlRererence = 'https://www.facebook.com' + cadena[urlBase:finUrl]

				if(findData > 1):
					urlImage = cadena[findData+11:findData+210]
					putDataCsv(urlRererence,urlImage,file)
				else:
					putDataCsv(urlRererence,'',file)



def putDataCsv(urlR,urlI,file):

	salida = csv.writer(file)
	salida.writerow([urlR,urlI])
	# salida.writerow('\r')
		   
	del salida
