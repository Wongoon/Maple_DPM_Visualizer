import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("maple_dpm.csv")

plt.plot(df['직업이름'], df['DPM'])
plt.show()