#aishnabest
#⭐⭐

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/GirishVerm/Stock_Prediction_Model/main/AAPL%20(1).csv", header=None)

yarray = np.array([0,1,6,4,7,2,7,5,4])

plt.plot(yarray, marker = 'o')

#plt.show()

print(data)
