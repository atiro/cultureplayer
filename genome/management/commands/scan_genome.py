import nltk
import os
import requests
import re
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup, Comment

from culture.models import Object
from genome.models import Channel, Programme
from django.core.management.base import NoArgsCommand, CommandError

genome_url = "http://genome.ch.bbc.co.uk"
genome_search_url = genome_url + "/search/0/20"

query_params = {
	"adv": 0,
	"q": None,
	"media": "all",
	"yf": "1923",
	"yt": "2009",
	"mf": "1",
	"mt": "12",
	"tf": "00:00",
	"tt": "00:00"
}

query_cache = {}

class Command(NoArgsCommand):
        help = "Loads objects from json data"

	def handle_noargs(self, **options):

	  for obj in Object.objects.filter(id__gt=2):
	    query_words = []
	    tokens = nltk.word_tokenize(obj.title)
	    tagged = nltk.pos_tag(tokens)
	    for tag in tagged:
	        if tag[1] == 'NNP':
	       	    query_words.append(tag[0])

	    print "Querying object ", obj.id

	    if len(query_words) < 1:
		print "No search words found, skipping (" + obj.title + ")"
		continue	
	    elif len(query_words) < 2:
		print "Too few words for search, skipping ("+query_words[0]+")"
		continue	

	    query_params["q"] = ' '.join(query_words)

#	if query_cache.has_key(query_params["q"]):
#	query_cache[query_params["q"]] = None

	    r = requests.get(genome_search_url, params=query_params)

	#print "Querying Genome: " + r.url

	    query_soup = BeautifulSoup(r.text, 'lxml')
	    results = query_soup.find_all('div', 'result')

	#print query_soup.title
	#print str(len(results)) + "matching programmes"

	    for result in results:
	        match_datetime = "(\d{4})-(\d{2})-(\d{2})#at-(\d{1,2})\.(\d{2})"

	        for element in result(text=lambda text: isinstance(text, Comment
)): 
			element.extract()

		channel_logo = result.img['alt']
	        title = ' '.join(result.find('a', 'title').stripped_strings)
	        url = result.h2.div.a['href']

	        match = re.search(match_datetime, url)
	        year = int(match.group(1))
	        month = int(match.group(2))
	        day = int(match.group(3))
	        hour = int(match.group(4))
	        mins = int(match.group(5))

	        description = ' '.join(result.stripped_strings)

	        channel, created = Channel.objects.get_or_create(title=channel_logo)

		if created:
			print "Created channel ", channel_logo

	        programme, created = Programme.objects.get_or_create(
				title=title, description=description,
				genome_url=url, datetime=datetime(year, month, day, hour, mins),
				channel = channel)

	        if not created:
		# Append our cultural object to existing Programme
		    print "Added object to existing programme"
		else:
		    print "Created new programme and added object"

		programme.related_objects.add(obj)
	# Now give genome a break
	    sleep(5)
