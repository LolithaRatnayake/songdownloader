#!/usr/bin/env python
from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import urllib, os

main_html = Browser().open("http://www.sinhalasongs.lk/sinhala-songs-download/sunil-edirisinghe/").read()
main_soup = BeautifulSoup(main_html)

alldivs = main_soup.findAll('div')

for song in alldivs[19:95]:
  temphtml = Browser().open(song.a['href'])
  tempsoup = BeautifulSoup(temphtml)
  save_as = os.path.join("./", song.a.text+".mp3" )
  urllib.urlretrieve(tempsoup.findAll('a')[15]['href'],save_as)
  print song.a.text+".mp3"

