from stardist.models import StarDist2D
from stardist.data import test_image_nuclei_2d
from stardist.plot import render_label
from csbdeep.utils import normalize
import matplotlib.pyplot as plt
from skimage.segmentation import find_boundaries
from tifffile import imread
from skimage.color import label2rgb
import os
from glob import glob
import pandas as pd 

'''
Copyright (c) 2024 Nathan Wood <contact@nwoodweb.xyz>

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

'''

# select 2D fluorescent nuclei model
model = StarDist2D.from_pretrained('2D_versatile_fluo')

# set input file directory and saved image directory 
imageDirectory = os.path.expanduser("/home/woodn/Desktop/viabilityph/DAPI")
saveDirectory = os.path.expanduser("/home/woodn/Desktop/viabilityph/counted-dapi")
saveReadsCSV = os.path.join(saveDirectory,"dapi.out")

# create dataframe
data =  []


# iterate each image and return cell count
for img in sorted(glob(os.path.join(imageDirectory,"*.tif"))):
    day = img[49:]
    day = day[:5]
    ph = img[45:]
    ph = ph[:3]
    image = imread(img)
    image = normalize(image,1,99.8)         # NORMALIZE FLUOR INTENSITY
    labels, cells = model.predict_instances(image,
        scale=1,
        return_labels=True)             # THIS IS THE MODEL 
    probability = list(cells["prob"])
    n_detections = len(probability)     # THE LENGTH OF PROBABILITY VECTOR IS THE CELL COUNT
    print('\n')
    print(f'{img},{day},{ph},{n_detections}')     
    data.append([day,ph,img, n_detections])    # STORE CELL COUNT WITH FILE NAME

    fig, ax = plt.subplots(figsize=(15,15))
    ax.imshow(label2rgb(labels,image=image,bg_label=0))
    plt.axis('off')
    plt.show()
    
# Write data to TSV
dataFrame = pd.DataFrame(data, columns = ["DAY","PH","FILENAME","COUNT"])
dataFrame.to_csv(saveReadsCSV, sep='\t', encoding='utf-8') 
