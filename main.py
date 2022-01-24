from turtle import title
import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"

#Get the HTML
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

#Parse the HTML
soup = BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)

title = soup.title
#print(title)

paras = soup.find_all('p')
#print(paras)
anchortags = soup.find_all('a')
print(anchortags)