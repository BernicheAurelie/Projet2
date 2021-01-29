import csv
import requests
from bs4 import BeautifulSoup 

links = []

for i in range (51):
 # on a 50 pages (première=page1, dernière = 50)
    url = 'http://books.toscrape.com/catalogue/page-' + str(i) + '.html' 
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.content, 'lxml')
        articles = soup.findAll('article')
        
        for article in articles:
            a = article.find('a')
            link = a['href']
            links.append('http://books.toscrape.com/' + link) 
            # concaténation url de base avec la portion de code fournie par href  

            # fonction open pour ouvrir un fichier (.csv) + 2e argt ,'w' pour lui dire de passer en mode écriture
            # ensuite on va prendre chacune de nos url et l'imprimer à l'int de ce .csv "\n" = retour à la ligne
with open ('urls.csv', 'w') as file:
    for link in links:
        file.write(link + '\n')
        




    