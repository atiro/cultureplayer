import json
import nltk
import os
from pprint import pprint
import requests
from bs4 import BeautifulSoup, Comment
from culture.models import Object,Institution,Location
import re
from genome.models import Channel, Programme
from django.core.management.base import NoArgsCommand, CommandError


lookup = []
npg_url = "http://www.npg.org.uk"
npg_search_url = npg_url + "/collections/search/person-list.php"

query_params = {
	"firstRun": "true",
	"name": "",
	"search": "aas",
	"gender": "",
	"desc": "",
	"occ": "",
	"place": "",
	"grp": "",
	"searchCatalogue": "Later Victorian Portraits",
	"submitSearchTerm_x": 53,
	"submitSearchTerm_y": 12,
	"submitSearchTerm": "Search Now",
	"displayNo": 60,
	"page": 0
}

#	//div[@class="result"]/img[@title] = channel
#	//div[@class="result"]/h2/a[@class="title"] = title
#	//div[@class="result"]/h2/div[@class="date-time"]/a = date_time
#	//div[@class="result"]/text*( = description
#

# Terrible hardcoding!

location = Location.objects.get(id=71)

class Command(NoArgsCommand):
      help = "Loads objects from NPG crawl"

      def handle_noargs(self, **options):

	for page in [0,1,2]:
	  query_params["page"] = page
	  r = requests.get(npg_search_url, params=query_params)
	  print "Querying NPG: " + r.url
	  query_soup = BeautifulSoup(r.text, 'lxml')
	  results = query_soup.find_all('div', 'eventsItem')
	  print query_soup.title
	  print str(len(results)) + "matching people"
	  for result in results:
		match_npgid = "(mp\d{5})"

		# Cleanup - remove comment tags
		for element in result(text=lambda text: isinstance(text, Comment)):
			element.extract()

		a = result.find('a', 'portraitExtended')
		pic_url = a['href']
		print "Got Pic URL: " + pic_url

		m = re.search(match_npgid, pic_url)
		npg_id = m.group(1)

		p = result.find('p', 'eventHeading')
		print "Portrait: " + ' '.join(p.a.strings)

		npg_search2_url  = npg_url + "/collections/search/personextended.php"

		query2_params =  { "linkid": npg_id, "page": 0 }

		r2 = requests.get(npg_search2_url, params=query2_params)

		print "Querying NPG: " + r2.url

		query_soup2 = BeautifulSoup(r2.text, 'lxml')

		results = query_soup2.find_all('div', 'eventsItem')

		print str(len(results)) + " matching portraits"

		for portrait in results:
			match_purl = ".*(mw\d{5,6})\.jpg"

                        img = portrait.find('div', 'image')
                        portrait_page = img.a["href"]

                        portrait_img = img.a.img["src"]
			m2 = re.match(match_purl, portrait_img)
			if m2:
			  portrait_id = m2.group(1)
			
                        print "Got portrait url: " + portrait_img
                        info = portrait.find('div', 'eventsDesc')
                        title = info.findAll('p')[0]
                        title = ' '.join(title.strings)
                        print "Got title: " + title
                        artist = info.findAll('p')[1]
                        artist_name = ' '.join(artist.strings)
                        clean_name = "\s*by\s+([a-zA-z' ]+)"
                        m3 = re.search(clean_name, artist_name)

                        if m3:
                                clean_artist =  m3.group(1)
                        else:
                                clean_artist = artist_name

			o = Object(title=title, artist=clean_artist,location=location, description="", collection_id=portrait_id, url= portrait_page, image_url=portrait_img)
			o.save()

		
