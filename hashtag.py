import numpy as np 
import pandas as pd

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

train = pd.read_csv("/kaggle/input/crowdflower-weather-twitter/train.csv")
test = pd.read_csv('/kaggle/input/crowdflower-weather-twitter/test.csv')
print(train.shape)
