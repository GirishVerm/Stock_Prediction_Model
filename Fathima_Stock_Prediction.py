#✰ #new attempt

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("https://github.com/GirishVerm/Stock_Prediction_Model/blob/main/AAPL%20(1).csv",on_bad_lines='skip')

print(data)

yarray = np.array([0,1,6,4,7,2,7,5,4])

plt.plot(yarray, marker = 'o')

plt.show()