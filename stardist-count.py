''' 
2025 WOOD-NT contact@nwoodweb.xyz
BSD-3 CLAUSE LICENSE

This script iterates an entire directory of fluorescence
tiff files, presumable separated into their own channels,
and uses StarDist to count each cell nuclei in the viewframe,
and then outputs the counts per image into separate files
per fluorescence channel used. 

RETURNS
-------

<date_experiment>-dapi-processed.csv: CSV ASCII text
    output csv of cell nuclei counted on the dapi channel.
    Hoechst 33342 permeates all cells, therefore counted
    cells in this channel represents the total number of
    cells in the image viewframe

<date_experiment>-fitc-processed.csv: CSV ASCII text
    output csv of cell nuclei counted on the fitc channel.
    SYTOX green permeates only dead and dying cells, therefore
    counted nuclei in this channel represents number of
    dead cells in the same image viewframe as the corresponding
    dapi channel.

USER DEFINED PARAMETERS
-----------------------

date_experiment: string
    date of which the experiment is conducted. This is critical
    to avoid confusing iterations

input_directory: string
    directory where TIF files are stored

model: string, default: StarDist2D.from_pretrained('2D_versatile_fluo')
    select the included pretrained stardist model for analysis. To
    analyze cell viability via differential nuclear flurochromes,
    use the 2D_versatile_fluo model

output_directory: string, default: "./"
    define the directory the data csv will be written to 

ph: split string
    this is my experimental groups, it is stripped out of the 
    filename and will need be altered to suit differences in 
    file naming and organization

time_point: split string
    this is my time points, it is stripped out of the 
    filename and will need be altered to suit differences in 
    file naming and organization

'''

import os
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
from skimage.segmentation import find_boundaries
from tifffile import imread
from skimage.color import label2rgb

# stardist specific libraries
from csbdeep.utils import normalize
from stardist.models import StarDist2D
from stardist.data import test_image_nuclei_2d
from stardist.plot import render_label

# select 2D fluorescent nuclei model
model = StarDist2D.from_pretrained('2D_versatile_fluo')

# set input file directory and saved image directory 
input_directory = os.path.expanduser("./tiffs/")
input_directory_dapi = os.path.join(input_directory, "*DAPI.tif")
input_directory_fitc = os.path.join(input_directory, "*FITC.tif")
output_directory = os.path.expanduser("./")
date_experiment = "11-11-1111"

output_file_dapi = date_experiment + "-dapi-processed.csv"
output_file_fitc = date_experiment + "-fitc-processed.csv"
output_file_dapi = os.path.join(saveDirectory,output_file_dapi)
output_file_fitc = os.path.join(saveDirectory,output_file_fitc)

# create empty dataframe
data_dapi =  []
data_fitc =  []

# iterate each image and return cell count
for img in sorted(glob(input_directory_dapi)):
    '''
    USER DEFINED PARAMETERS

    These parameters strip part of the filename string to derive
    categories that will later constitutes columns, because
    your filename style and/or experimental groups may be different
    you will most likely need to modify these.
    '''
    time_point = img[49:54]
    ph = img[45:48]

    # read image
    image = imread(img)
    
    # histogram equalization
    image = normalize(image,1,99.8)
    
    # segmentation via 2D fluorescence stardist model
    labels, cells = model.predict_instances(image,
        scale=1,
        return_labels=True)
    
    # the number of detected objects is length of the probabilities
    # list
    probability = list(cells["prob"])
    n_detections = len(probability)

    # write data into empty dataframe
    data_dapi.append([time_point,ph,img, n_detections])

# FITC 
for img in sorted(glob(input_directory_fitc)):
    '''
    USER DEFINED PARAMETERS

    These parameters strip part of the filename string to derive
    categories that will later constitutes columns, because
    your filename style and/or experimental groups may be different
    you will most likely need to modify these.
    '''
    day = img[49:54]
    ph = img[45:48]

    # read image
    image = imread(img)
    
    # histogram equalization
    image = normalize(image,1,99.8)
    
    # segmentation via 2D fluorescence stardist model
    labels, cells = model.predict_instances(image,
        scale=1,
        return_labels=True)
    
    # the number of detected objects is length of the probabilities
    # list
    probability = list(cells["prob"])
    n_detections = len(probability)

    # write data into empty dataframe
    data_fitc.append([day,ph,img, n_detections])


# Write data to CSV
dataframe_dapi = pd.DataFrame(data_dapi, columns = ["DAY","PH","FILENAME","COUNT"])
dataframe_fitc = pd.DataFrame(data_fitc, columns = ["DAY","PH","FILENAME","COUNT"])
dataframe_dapi.to_csv(output_file_dapi, sep=',', encoding='utf-8')
dataframe_fitc.to_csv(output_file_fitc, sep=',', encoding='utf-8')
