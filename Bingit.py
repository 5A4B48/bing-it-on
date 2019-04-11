import requests
import json
import webbrowser
import time
import random

terms = []


def getterms():
	a = requests.get('https://corporatebs-generator.sameerkumar.website/')
	b = json.loads(a.content.decode('latin-1'))
	c = b.get('phrase').split()
	return c

		
while len(terms) < 31:
	d = getterms()
	for i in d:
		terms.append(i)


for q in terms:
	webbrowser.open("https://bing.com/search?q=" + q)
	time.sleep(random.randint(1, 3))


