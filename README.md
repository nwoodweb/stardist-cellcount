# Assessing Cell Viability Using StarDist to Count Two Different Fluorescent Nuclei Stains

## Introduction

The goal of these scripts is to

1. Automate fluorescent nuclei counting for two channels, DAPI and FITC. This is based
on the idea that our viability assays employ Hoescht33342 (DAPI), which should permeate
all cells, and SYTOX Green (FITC), which should only permeate dead cells. Cell
viability in this case can be represented as fractional viability:

$$ Viability = \frac{Total - Dead}{Total} $$
$$ Viability = \frac{DAPI - FITC}{DAPI} $$ 

2. Return two CSV files, one per fluorescence channel, which can then be merged
and processed for analysis.

## Installation

**These instructions assume you are operating in a Windows Subsystem For Linux
or Linux environment**

0. To establish the required conda environment, please either follow [my own
instructions](./install.md) or use the [StarDist provided installation](https://github.com/stardist/stardist/tree/main).

1. In the desired directory, run the following git clone

`git clone https://github.com/nwoodweb/stardist-cellcount.git`

2. Activate the requisite conda environment

`conda activate <environment_name>`

3. Execute the Jupyter Notebook environment

`jupyter notebook`

4. Then navigate to open the desired `.ipynb` notebook.

## StarDist is a Program Developed by Uwe Schmidt, and Martin Weingert

Please provide credit to the authors of the original StarDist program. 
The original StarDist can be found here: [https://github.com/stardist/stardist/tree/main](https://github.com/stardist/stardist/tree/main)

```
@inproceedings{schmidt2018,
  author    = {Uwe Schmidt and Martin Weigert and Coleman Broaddus and Gene Myers},
  title     = {Cell Detection with Star-Convex Polygons},
  booktitle = {Medical Image Computing and Computer Assisted Intervention - {MICCAI} 
  2018 - 21st International Conference, Granada, Spain, September 16-20, 2018, Proceedings, Part {II}},
  pages     = {265--273},
  year      = {2018},
  doi       = {10.1007/978-3-030-00934-2_30}
}

@inproceedings{weigert2020,
  author    = {Martin Weigert and Uwe Schmidt and Robert Haase and Ko Sugawara and Gene Myers},
  title     = {Star-convex Polyhedra for 3D Object Detection and Segmentation in Microscopy},
  booktitle = {The IEEE Winter Conference on Applications of Computer Vision (WACV)},
  month     = {March},
  year      = {2020},
  doi       = {10.1109/WACV45572.2020.9093435}
}

@inproceedings{weigert2022,
  author    = {Martin Weigert and Uwe Schmidt},
  title     = {Nuclei Instance Segmentation and Classification in Histopathology Images with Stardist},
  booktitle = {The IEEE International Symposium on Biomedical Imaging Challenges (ISBIC)},
  year      = {2022},
  doi       = {10.1109/ISBIC56247.2022.9854534}
}
```
