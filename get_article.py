from bs4 import BeautifulSoup

def get_article(article):
    a = article.find('a')
    link = a['href']
    url_article = link.replace('../../../', 'http://books.toscrape.com/catalogue/')
    return url_article

#url_article = get_article.get_article(article)
#links.append(url_article)
