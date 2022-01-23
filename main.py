import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"

#Get the HTML
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

#Parse the HTML
soup = BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify)
