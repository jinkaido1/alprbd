# ALPR - Bangladesh

***Thesis**: Automated Bangla License Plate Recognition.*

This branch was created to generated dataset for OCR. 

## Setup 
- Install `anaconda3`
- Install `opencv3`: `conda install -c menpo opencv3` 
- Clone this repository: `git clone git@github.com:dipu-bd/ALPR-Bangladesh.git`

# Plans

Standard license plates have 3 parts:    
- City or metropolitan name.
- A letter indicating vehicle type.
- 6 digits of plate number

We are going to build two types of recognizer:   
- Bangla digit recognition.
- Bangla letter recognition.

The city name shall be guessed from these variables:
- Number of strings
- Number of characters
- Appearance of specific letters at a specific position
- Appearance of KARs and FOLAs.

The recognition part shall be done using a feed-forward multi-layer neural network. We shall implement the system in TensorFlow. Dataset generated by the [dataset](https://github.com/dipu-bd/alpr-bd/tree/dataset) shall be used here.

After training the weight matrix will be stored in a file, which we will use later in our original project.
