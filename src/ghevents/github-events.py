#!/usr/bin/env python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

def retrieve_events(url):
	"""Returns a list of dictionaries containing event information."""
	response = requests.get(url).text
	print(response)
	events = json.loads(response)
	return events

def print_events(events, n=5):
	"""Prints the first n events."""
	for x in events[:n]:
   		 event = x['type'] + ' :: ' + x['repo']['name']
   		 print(event)

def main():
	print(GHUSER)
	print(url)
	list_events = retrieve_events(url)
	print_events(list_events, 10)

if __name__ == "__main__":
    main()
