import utils
import requests
from bs4 import BeautifulSoup 



def get_upc(soup):
    upc = soup.find('td').text
    return upc
def get_title (soup):
    title = soup.find('h1').text
    return title
def get_product (soup):
    product = soup.find("article", "product_page")
    return product
def get_url_image (soup):
    product = soup.find("article", "product_page")
    image = product.img["src"] .replace("../..", "http://books.toscrape.com")
    return image
def get_review_rating (soup):
    product = soup.find("article", "product_page")
    review_rating = product.find("p", "star-rating")["class"][-1]
    return review_rating
def get_category (soup):
    category = soup.find('ul').find_all('a')[2].text
    return category
def get_number_available (soup):
    number_available = soup.find('p', {'class':'instock availability'}).text.strip()
    return number_available
def get_price_excl_tax (soup):
    tds = soup.findAll('td')
    liste = []
    for td in tds:
        liste.append(td.text)
    price_excl_tax = liste[2]
    return price_excl_tax
def get_price_incl_tax (soup):
    tds = soup.findAll('td')
    liste = []
    for td in tds:
        liste.append(td.text)
    price_incl_tax = liste[3]
    return price_incl_tax
def get_product_description (soup):
    ps = soup.findAll ('p')
    liste_p = []
    for p in ps:
        liste_p.append(p.text)
    product_description = liste_p[3]
    return product_description

def scrap_book(url):
    book = dict()
    soup = utils.request(url)
    book["product_page_url"] = url
    book["title"] = get_title(soup)
    book["url_image"] = get_url_image(soup)
    book["category"] = get_category(soup)
    book["upc"] = get_upc(soup)
    book["review_rating"] = get_review_rating(soup)       
    book["number_available"] = get_number_available(soup)      
    book["price_excl_tax"] = get_price_excl_tax(soup)
    book["price_incl_tax"] = get_price_incl_tax(soup)
    book["product_description"] = get_product_description (soup)
    return book