import pandas as pd
import numpy as np
pd.set_option("display.max_columns", None)
import warnings
warnings.filterwarnings("ignore")

# other
import string
import math
import missingno as msno

import xgboost



if __name__=="__main__":
    songs_df = pd.read_csv("../data/songs.csv")
    songs_extra_df = pd.read_csv("../data/song_extra_info.csv")

    pass
