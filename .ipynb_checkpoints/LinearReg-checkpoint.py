import pandas as pd 
import numpy as np
import matplotlib.pyplot as plot
from sklearn import linear_model

df = pd.read_csv("homeprices.csv")
print(df)
df.plot.line()
