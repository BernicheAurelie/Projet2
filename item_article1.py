import requests
from bs4 import BeautifulSoup 
import csv

links = []
url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = requests.get(url)
if response.ok:
    soup = BeautifulSoup(response.content, 'lxml') 
    upc = soup.find('td').text
    title = soup.find('h1').text
    article = soup.find("article", "product_page")
    image = article.img["src"] .replace("../..", "http://books.toscrape.com")
    rating = article.find("p", "star-rating")["class"][-1]
    category = soup.find('ul').find_all('a')[2].text
    number_available = soup.find('p', {'class':'instock availability'}).text.strip()  
    tds = soup.findAll('td')
    liste = []
    for td in tds:
        liste.append(td.text)
    price_excl_tax = liste[2] 
    price_incl_tax = liste[3]
    ps = soup.findAll ('p')
    liste_p = []
    for p in ps:
        liste_p.append(p.text)
    product_description = liste_p[3]
    print (product_description)
    book = {"category": category, "title": title, "url_image": image,
            "upc": upc, "review_rating": rating, "disponibility": number_available,
            "Price_excl_tax": price_excl_tax, "Price_incl_tax": price_incl_tax,
            "product_description": product_description}

    with open('book_1.csv', 'w', newline='') as file:
        fieldnames = ["category", "title", "url_image","upc", "review_rating", "disponibility", 
                      "Price_excl_tax", "Price_incl_tax", "product_description"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(book)

    

