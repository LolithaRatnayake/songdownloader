#!/usr/bin/env python
from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import urllib, os

html = Browser().open("http://web.jayasrilanka.net/2015/01/gunadasa-kapuge-130-best-sinhala-mp3.html").read()
soup = BeautifulSoup(html)

ul = soup.findAll('ul')
listitems = ul[2].findAll('li')

for li in listitems:
  save_as = os.path.join("./", li.b.text )
  urllib.urlretrieve("http://jayasrilanka.info/albums/Gunadasa-Kapuge/"+ li.b.text,save_as)
  print li.b.text

