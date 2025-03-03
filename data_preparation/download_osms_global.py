from os import mkdir
from os.path import join, isdir, isfile
import wget
from multiprocessing import Pool

osmdir = 'osms'
if not isdir(osmdir):
	mkdir(osmdir)

url = "https://download.geofabrik.de/africa/{}-latest.osm.bz2"
# url = "https://download.geofabrik.de/central-america/{}-latest.osm.bz2"
# url = "https://download.geofabrik.de/asia/{}-latest.osm.bz2"

countries = ['algeria', 'angola', 'benin', 'botswana', 'burkina-faso', 'burundi', 'cameroon', 'cape-verde', 'central-african-republic', 'chad', 'comoros', 'congo-brazzaville', 'congo-kinshasa', 'djibouti', 'egypt', 'equatorial-guinea', 'eritrea', 'eswatini', 'ethiopia', 'gabon', 'gambia', 'ghana', 'guinea', 'guinea-bissau', 'ivory-coast', 'kenya', 'lesotho', 'liberia', 'libya', 'madagascar', 'malawi', 'mali', 'mauritania', 'mauritius', 'morocco', 'mozambique', 'namibia', 'niger', 'nigeria', 'rwanda', 'sao-tome-and-principe', 'senegal', 'seychelles', 'sierra-leone', 'somalia', 'south-africa', 'south-sudan', 'sudan', 'tanzania', 'togo', 'tunisia', 'uganda', 'zambia', 'zimbabwe']
states = ['cambodia']

def download(state):
	fname = url.format('-'.join(state.lower().split(' ')))
	print(fname)
	if not isfile(join(osmdir, fname.split('/')[-1])):
		filename = wget.download(fname, out=osmdir)
	print('Done with {}'.format(state))

with Pool() as pool:
	pool.map(download, states)