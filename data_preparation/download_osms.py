from os import mkdir
from os.path import join, isdir, isfile
import wget
from multiprocessing import Pool

osmdir = 'osms'
if not isdir(osmdir):
	mkdir(osmdir)

url = "https://download.geofabrik.de/north-america/us/{}-latest.osm.bz2"


# states = ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
states = ['Indiana']
def download(state):
	fname = url.format('-'.join(state.lower().split(' ')))
	print(fname)
	if not isfile(join(osmdir, fname.split('/')[-1])):
		filename = wget.download(fname, out=osmdir)
	print('Done with {}'.format(state))

with Pool() as pool:
	pool.map(download, states)