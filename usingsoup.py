from bs4 import BeautifulSoup
import requests,re

symbol=raw_input('Enter the symbol Name:')

myurl='http://finance.yahoo.com/q/op?s=' + symbol + "+ Options"

html = requests.get(myurl).content
soup=BeautifulSoup(html,"html.parser")
print soup.find('span',attrs={'class':'Fw(b) D(ib) Fz(36px) Mb(-4px)'} ).text