import json
import re
import requests
from bs4 import BeautifulSoup

url = "https://signup.mail.com/"

response = requests.get(url)

print(response.status_code)


data = response.text


soup = BeautifulSoup(data, 'html.parser')
print(soup.prettify())

pattern = re.compile(r"\[.*\]")


domains = soup.find(id="application-config")
result = soup.find("domains", text=pattern)


print(result)
print("\n")
