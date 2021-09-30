from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.huiles-et-sens.com/en/")
soup = BeautifulSoup(page.content, "html.parser")
all_product = soup.find_all(class_="mo_ml_level_0 mo_ml_column")

for products in all_product:
    for link in products.find_all("a", href=True):
        links = (link["href"])
        clean_links = links.replace("javascript:;", "").replace("javascript:setCurrency(3);","")
        print(clean_links)


