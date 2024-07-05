# %% Modules

import glob
import numpy as np
import matplotlib.pyplot as plt

# %% Get a list of all the *.tiff images

raw_data_path = "../../Data/Raw_Tiff"
raw_data_files = glob.glob("%s/*" % (raw_data_path))

# %% Apply convolution

# %%
