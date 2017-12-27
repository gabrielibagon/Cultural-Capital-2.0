import csv
import json
import urllib.request
import os.path

baseURL = "http://www.metmuseum.org/api/Collection/additionalImages?crdId="

with open("MetObjects.csv",'r') as f:
	reader = csv.reader(f,delimiter=',')
	next(reader)
	for line in reader:
		publicDomain = line[2]
		if publicDomain:
			itemID = line[3]
			fullURL = baseURL + itemID
			jsonResponse = json.loads(urllib.request.urlopen(fullURL).read().decode('utf-8'))['results']
			if jsonResponse:
				imageURL = jsonResponse[0]['webImageUrl']
				title = jsonResponse[0]['title']
				if not title:
					title = itemID
				filename = 'artworks/' + title + '.jpg'
				if not os.path.isfile(filename):

					try:
						urllib.request.urlretrieve(imageURL,filename)
					except Exception as e:
						print(e)