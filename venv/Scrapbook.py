"""
scraper livre
    [x] product_page_url
    [x] universal_ product_code (upc)
    [x] title
    [x] price_including_tax
    [x] price_excluding_tax
    [x] number_available
        recuperer le chiffre
    [x] product_description
    [x] category
    [x] review_rating
    image_url

scraper category


scraper le site


"""

import requests
from bs4 import BeautifulSoup
import csv

book_url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
url = requests.get(book_url)
soup = BeautifulSoup(url.content, "html.parser")
first_img_link = "https://books.toscrape.com"
second_img_link = "../../media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg"
img_url = f"{first_img_link}{second_img_link[5:]}"

# Fonction qui récupère les informations d'un livre

def scrap_book(book_url):

    book_data = {}
    book_data["url"] = book_url
    book_data["title"] = soup.h1.text
    book_data["upc"] = soup.find_all("td")[0].text
    book_data["price_excl_tax"] = soup.find_all("td")[2].text
    book_data["price_incl_tax"] = soup.find_all("td")[3].text
    book_data["stock_available"] = soup.find_all("td")[5].text
    book_data["product_description"] = soup.find_all("p")[3].text
    book_data["category"] = soup.find_all("a")[3].text
    book_data["review_rating"] = soup.find_all("td")[6].text
    book_data["img_url"] = img_url
    return book_data

print(scrap_book(book_url))




# Fonction qui récupère les catégories

category_url = "https://books.toscrape.com/index.html"
url = requests.get(category_url)
soup = BeautifulSoup(url.content, "html.parser")


def scrap_category(category_url):

    book_category = {}
    book_category["url"] = category_url
    book_category["category"] = soup.find_all("a")
    return book_category


print(scrap_category(category_url))
