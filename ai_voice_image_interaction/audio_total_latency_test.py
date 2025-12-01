import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Ossian Audio Latency Tests.csv")
data1 = pd.read_csv("Meta Latency Tests.csv")
data2 = pd.read_csv("Even G1 Audio Latency Tests.csv")
data3 = pd.read_csv("HeyCyan Audio Latency Tests.csv")

# Get data
data =  data["Latency (s)"]
data1 =  data1["Total Latency (s)"]
data2 = data2["Latency (s)"]
data3 = data3["Actual Latency"]

print(np.median(data), np.std(data), np.var(data), "\n")
print(np.median(data1), np.std(data1), np.var(data1), "\n")
print(np.median(data2), np.std(data2), np.var(data2), "\n")
print(np.median(data3), np.std(data3), np.var(data3), "\n")

# Sort the data
sorted_data = np.sort(data)
sorted_data1 = np.sort(data1)
sorted_data2 = np.sort(data2)
sorted_data3 = np.sort(data3)

# Calculate CDF
cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
cdf1 = np.arange(1, len(sorted_data1) + 1) / len(sorted_data1)
cdf2 = np.arange(1, len(sorted_data2) + 1) / len(sorted_data2)
cdf3 = np.arange(1, len(sorted_data3) + 1) / len(sorted_data3)

# Statistical Features
latency_mean = np.mean(data)
latency_median = np.median(data)
latency_std = np.std(data)
latency_var = np.var(data)
# print(f"Latency mean: {latency_mean:.2f}, Latency median: {latency_median:.2f}, Latency standard deviation: {latency_std:.2f}, Latency variance: {latency_var:.2f}")

# Plot CDF
Meta_Glass = plt.plot(sorted_data1, cdf1, linewidth=7, color="blue", label="RB-Meta")
Even_Glass = plt.plot(sorted_data2, cdf2, linewidth=7, color="black", label="Even G1")
Dragon_Glass = plt.plot(sorted_data, cdf, linewidth=7, color="red", label="Dragon")
HeyCyan_Glass = plt.plot(sorted_data3, cdf3, linewidth=7, color="cyan", label="Cyan")
plt.scatter(sorted_data, cdf, s=10, color="black")
plt.xlabel('AI Voice Interaction Latency (s)', fontsize=40)
plt.ylabel('CDF', fontsize=40)
plt.tick_params(axis="both", labelsize="40")
plt.xlim(0, 14)
plt.ylim(0, 1)
plt.grid(True)

plt.subplots_adjust(left=.2,bottom=.2)
plt.legend(fontsize="30", loc="lower right")
plt.show()