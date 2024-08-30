import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract data from the Web Page
data = soup.find("div", {"class": "data-container"}).text
print(data)