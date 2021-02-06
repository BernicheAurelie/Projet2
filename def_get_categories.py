from bs4 import BeautifulSoup
import utils

def get_categories (bookstoscrap):
    soup = utils.request(bookstoscrap)
    cat = soup.find_all("a")
    links_category = []
    for link in cat:
        category = link.get("href")
        category_url = category.replace("../books", "http://books.toscrape.com/catalogue/category/books")    
        links_category.append(category_url)
    categories_url = links_category[3:53]
    return categories_url
    
# bookstoscrap = 'http://books.toscrape.com/catalogue/category/books_1/index.html'