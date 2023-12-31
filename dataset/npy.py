import os
from PIL import Image
import json
import shutil
import numpy as np
import pickle  # Import pickle module

# Path to your .pkl file
pkl_path = '/media/hongji/4T/Downloads/3DPW/sequenceFiles/sequenceFiles/train/courtyard_backpack_00.pkl'

# Open the .pkl file in binary read mode
with open(pkl_path, 'rb') as file:
    data = pickle.load(file, encoding='latin1')

# Now you can print or work with the data
print(data.keys())
print(data['betas'])
print(data['poses'][0])
