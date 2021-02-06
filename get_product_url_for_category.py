from bs4 import BeautifulSoup
import utils
import get_article
import scraping
import dictwriter_csv

def get_product_url_for_category(category_url):
    links = []
    soup = utils.request(category_url)# r = requests.get(category_url)
    boutonNext = soup.find("li", {"class": "next"})
    index = 1
    articles = soup.find_all('article', 'product_pod')             
    for article in articles:
        url_article = get_article.get_article(article)
        links.append(url_article)
    while boutonNext is not None:
        index +=1
        category_url = category_url.replace("index.html", "page-" + str(index) + '.html')
        soup = utils.request(category_url)# r = requests.get(category_url)
        articles = soup.findAll('article', 'product_pod')             
        for article in articles:
            url_article = get_article.get_article(article)
            links.append(url_article)
        boutonNext = soup.find("li", {"class": "next"})
    for link in links:
        soup = utils.request(link)#r = requests.get(link)
        book = scraping.scrap_book(link)
        file = dictwriter_csv.write_csv(book)
    return file

category_url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
file = get_product_url_for_category(category_url)