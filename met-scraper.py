import csv
import json
import urllib.request
import os

base_url = "http://www.metmuseum.org/api/Collection/additionalImages?crdId="
artwork_dir = 'artworks/'

with open("MetObjects.csv",'r') as f:
	reader = csv.reader(f,delimiter=',')
	lastImg = sorted([int(x.split('.')[0]) for x in os.listdir('artworks')])[-1]
	next(reader)
	for line in reader:
		itemID = line[3].zfill(7)
		if int(itemID) <= int(lastImg):
			continue
		print(line)
		fullURL = base_url + itemID
		jsonResponse = json.loads(urllib.request.urlopen(fullURL).read().decode('utf-8'))['results']
		if jsonResponse:
			imageURL = jsonResponse[0]['webImageUrl']
			filename = itemID + '.jpg'
			filepath = os.path.join(artwork_dir,filename)
			if not os.path.isfile(filepath):
				try:
					urllib.request.urlretrieve(imageURL,filepath)
					print('Successfully Downloaded')
				except Exception as e:
					print(e)
			else:
				print("File already exists")
		else:
			print('Invalid file')
		print('\n')