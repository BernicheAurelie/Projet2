from bs4 import BeautifulSoup
import utils
import scraping
import dictwriter_csv

def get_product_url_for_category(category_url):
    links = []
    soup = utils.request(category_url)# r = requests.get(category_url)
    boutonNext = soup.find("li", {"class": "next"})
    index = 1
    articles = soup.find_all('article', 'product_pod')             
    for article in articles:
        a = article.find('a')
        link = a['href']
        url_article = link.replace('../../../', 'http://books.toscrape.com/catalogue/')
        links.append(url_article)
    while boutonNext is not None:
        index +=1
        category_url = category_url.replace("index.html", "page-" + str(index) + '.html')
        soup = utils.request(category_url)# r = requests.get(category_url)
        articles = soup.findAll('article', 'product_pod')             
        for article in articles:
            a = article.find('a')
            link = a['href']
            url_article = link.replace('../../../', 'http://books.toscrape.com/catalogue/')
            links.append(url_article)
        boutonNext = soup.find("li", {"class": "next"})
    for link in links:
        soup = utils.request(link)#r = requests.get(link)
        book = scraping.scrap_book(link)
        file = dictwriter_csv.write_csv(book)
    return file

