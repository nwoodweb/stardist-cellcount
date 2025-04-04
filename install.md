# Installing the StarDist Script 

Nathan Wood 2025

# Citing StarDist

StarDist github is here: <https://github.com/stardist/stardist>

StarDist is BSD-3 Licenses software, and it must be cited in any
publication where its use is employed. These three publications must be
included.

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

# Installation

## Prerequisite: Windows Subsystem for Linux

1.  Open Powershell by looking for it in the Windows Start Menu
2.  Run the following command:

```
    wsl --install 
```

Follow all instructions given, and write down both the user and root
passwords.

This will install the Windows-Linux compatability layer with the
recently approved Ubuntu distribution.

### WSL2: Where is my Filesystem?

1.  WSL2 creates a separate Ubuntu related file hierarchy. The Windows
    C: or D: drives are located under the partition:

```
    /mnt/<drivename>
```

where all of the files associated with your Windows OS are located.

2.  To make things more convenient, you may want to symbolically link
    your relevant Windows directories to corresponding Ubuntu
    directories. An example is included below


```
    cd ~/
    ln -s ../mnt/<drive>/<desired windows directory> ./<desired linux directory>
```
This can be confirmed by using:

```
    ls ./<desired linux directory>
```

in which the contents of the corresponding Windows directory should be
shown.

![Linux hierarchy, windows drives are symbollically linked to
/mnt](/home/woodn/Pictures/linux-filesystem.png)

## Prerequisite: Installing Git

Git is a software version control system. It may be already installed on
Ubuntu for WSL2. To confirm this, run the command:

```
    git -v
```

if an error is returned, you will need to install git using Ubuntu's
software package manager, Aptitude.

```
    sudo apt install git
```

If the command mentions " Not in sudoers file", this can be circumvented
by using `su` , entering the root password, then entering the above
command.

To add user to sudoers, while as root, enter the command

```
    adduser <username> sudo
```

you may need to use `/sbin/adduser` instead.

## Prerequisite: Installing Python 3

Python 3 is often already installed on most Linux systems. To confirm
this, enter the command

```
    python -V
```

You will likely need to install `pip` if not already installed:

```
    sudo apt install python3-pip
```

If Python 3 is not installed, entering the above command will install it
as a prerequsite.

## Prerequisite: Install Curl

Curl is a utility that pulls down web content. To make sure curl is
installed to the system, run the following command:

```
    curl -V
```

An output should be given, if an error is returned, run this command to
install it.

```
    sudo apt install curl
```

## Prerequisite: Installing MiniConda for WSL2

Miniconda allows packages of a specific version to be self-contained
from system-dependent python libraries. For WSL, it can be installed via
using the following commands, entered one at a time.

1.  Ensure system is up to date using `sudo apt update`, then
    `sudo apt upgrade`
2.  Return to home using `cd ~/`
3.  Run
    `curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`
4.  Output the file's 256 bit checksum
    `sha256sum ~/Miniconda3-latest-Linux-x86_64.sh`
5.  Check the checksum at <https://repo.anaconda.com/miniconda/>
6.  Execute the script `bash ~/Miniconda3-latest-Linux-x86_64.sh`.
7.  Follow the provided instructions, I would recommend keeping the
    default installation prefix. It may be convenient to have conda
    initialize whenever you open up WSL2 Ubunutu, if so, select yes at
    the final question. If not (default option), you can always start it
    by adding an alias to `~/.bashrc` by
    `echo alias condastart="~/miniconda3/bin/conda init"`, doing this
    will allow conda to initialize when entering `condastart`
8.  Reset Bash by using `source ~/.bashrc`

Conda should now be installed for WSL2 Ubuntu.

## Installing StarDist for Generic 64 Bit X86 CPUs

This should work on most consumer hardware.

1.  Make sure conda is initialized. The WSL Ubuntu command line should
    mention `(base)` somewhere, if not run
    `~/miniconda3/bin/conda init`.
2.  Create conda environment using the command
    `conda create -n stardist`
3.  Once complete, enter the conda environment using the command
    `conda activate stardist`
4.  Once in the conda environment, install TensorFlow 2 using command
    `conda install tensorflow`
5.  After installing tensorflow, install stardist using
    `pip3 install stardist`

Stardist should now be installed.

### Resolving TensorFlow Dependency Hell

If errors arise while either installing or executing stardist, you may
need to install tensorflow using `pip`

1.  Make sure you are in the `stardist` conda environment, see above
2.  First uninstall conda TensorFlow using `conda uninstall tensorflow`
3.  Then install TensorFlow using `pip3 install tensorflow`
4.  Check stardist either by installing or running the script again.

## Installing StarDist for Systems with Nvidia Graphics Cards

This is to install a StarDist version for systems that have Nvidia
graphics cards, and employs CUDA hardware acceleration.

To see if your Nvidia card is compatible, please check
<https://developer.nvidia.com/cuda-gpus>.

1.  Make sure conda is initialized. The WSL Ubuntu command line should
    mention `(base)` somewhere, if not run
    `~/miniconda3/bin/conda init`.
2.  Create the required conda environment via the following conda
    command:


```
    conda env create -f \
    https://raw.githubusercontent.com/CSBDeep/CSBDeep/main/extras/environment-gpu-py3.8-tf2.4.yml
```

3.  Enter the conda environment `csbdeep` via `conda activate csbdeep`
4.  Install stardist via `pip install stardist`

Stardist is now installed
