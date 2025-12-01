import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Ossian Audio Bitrate Test.csv")

# Get data
time =  data["Interval start"]
uplink = data["Uplink"]
downlink = data["Downlink"]

for i in range(len(time)):
    uplink[i] = uplink[i] / 1000
    downlink[i] = downlink[i] / 1000

# Plot
uplink_plot = plt.plot(time, uplink, label="Uplink", linewidth=7)
downlink_plot = plt.plot(time, downlink, label="Downlink", linewidth=7)
plt.xlabel('Time (s)', fontsize=55)
plt.ylabel('Bitrate (Kbps)', fontsize=55)
plt.xlim([0,17])
plt.ylim([0,1000])
plt.tick_params(axis="both", labelsize="50")
plt.grid(True)

plt.legend(fontsize="45",loc='upper left')
plt.show()