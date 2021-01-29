from bs4 import BeautifulSoup
import requests
import csv
import os.path

links = []
for i in range(1,6):
    url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/page-' + str(i) + '.html'
    r = requests.get(url)
    if r.ok:
        soup = BeautifulSoup(r.content, 'lxml')
        articles = soup.findAll('article', 'product_pod')
        
        for article in articles:
            a = article.find('a')
            link = a['href']
            url_article = link.replace('../../../', 'http://books.toscrape.com/catalogue/')
            links.append(url_article)

        for link in links:
            r = requests.get(link)
            if r.ok:
                product_page_url = link
                soup = BeautifulSoup(r.content, 'lxml')
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

                book = {"category": category, "title": title,"product_page_url": product_page_url, "url_image": image,
                        "upc": upc, "review_rating": rating, "disponibility": number_available,
                        "Price_excl_tax": price_excl_tax,"Price_incl_tax":price_incl_tax, "Product_description": product_description}
            
            with open('mystery_book_info.csv', mode='a+', encoding='UTF-8-sig') as file:
                writer = csv.DictWriter(file, fieldnames=book.keys(), delimiter=",")
                if os.path.getsize('mystery_book_info.csv') == 0:
                    writer.writeheader()
                writer.writerow(book)

