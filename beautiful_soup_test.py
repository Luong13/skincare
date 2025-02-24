import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)

# parse HTML content
soup = BeautifulSoup(response.content, "html.parser")

# find by tag name
title = soup.title.text

# find by class
paragraphs = soup.find_all("p", class_="article-text")

# find by ID
main_content = soup.find("div", id="main-content")

print(title)
print()
print(paragraphs)
print()
print(main_content)