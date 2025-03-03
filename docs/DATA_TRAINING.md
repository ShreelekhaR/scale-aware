# Data Preparation and Training Guide

<!-- first create links to data and then training -->
#
# ## Data Preparation
#
# To prepare the data for training, follow these steps:
Download raw osm files using `download_osms.py`
 > python download_osms.py

 This command will download all osm files in contiguous unites states. So 48 states+D.C. (no Hawaii and Alaska).

:warning: When testing do not download all states. Instead edit the list in variable `states` before downloading. Also use a smaller state's osm file such as Delaware or Vermont to first test.

Use the following comand to extract osm files.
> bash unzip_osm.sh

---
## Step-1: Locate Multilabel Image
`class_functions.py` and `efficient_v2_sentinel.py` are used for getting image centroids and segmentation. The input osm file needs to be in the same folder.

Run command: 
> python efficient_v2_sentinel.py -i [input filename]

to get `[filename].csv` and `[filename].npz`

---
## Step-2: Install gcloud and Earth Engine Authentication
You can follow this link to install gcloud and complete earth engine authentication: https://developers.google.com/earth-engine/guides/python_install#authentication


Run command: 
> python naip_sentinel_downloader.py

to get images at scale, at both 10m resolution and 100 corresponding 1m resolution imagery stored in directory `images`

This way of labeling of satellite imagery using OpenStreetMap (OSM) data can be credited to Mall et. al. in [Remote Sensing Vision-Language Foundation Models
without Annotations via Ground Remote Alignment](https://graft.cs.cornell.edu/). 

---
## Step-3: Prepare Data for Training
Run command:
> python prepare_train_data.py
to prepare data for training. This will create 4 CSV files: sentinel_train.csv, sentinel_val.csv, naip_train.csv, naip_val.csv

#
## Training
#
### Training High and Low Resolution Models

<!-- To train the fully supervised high resolution model, run the following command: -->
