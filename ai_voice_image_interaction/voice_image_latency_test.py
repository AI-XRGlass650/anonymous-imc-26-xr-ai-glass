import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Voice Image Latency Tests.csv")
data1 = pd.read_csv("Meta Image Latency Tests.csv")
data2 = pd.read_csv("HeyCyan Image Latency Tests.csv")

# Get data
data =  data["Latency (s)"]
data1 = data1["Total Latency (s)"]
data2 = data2["Actual Latency"]

print(np.mean(data))
print(np.mean(data1))
print(np.mean(data2))

# Sort the data
sorted_data = np.sort(data)
sorted_data1 = np.sort(data1)
sorted_data2 = np.sort(data2)

# Calculate CDF
cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
cdf1 = np.arange(1, len(sorted_data1) + 1) / len(sorted_data1)
cdf2 = np.arange(1, len(sorted_data2) + 1) / len(sorted_data2)

# Statistical Features
latency_mean = np.mean(data)
latency_median = np.median(data)
latency_std = np.std(data)
latency_var = np.var(data)
# print(f"Latency mean: {latency_mean:.2f}, Latency median: {latency_median:.2f}, Latency standard deviation: {latency_std:.2f}, Latency variance: {latency_var:.2f}")

# Plot CDF
plt.plot(sorted_data1, cdf1, linewidth=7, color="blue", label="Meta")
plt.plot(sorted_data, cdf, linewidth=7, color="red", label="Dragon")
plt.plot(sorted_data2, cdf2,linewidth=7, color="cyan", label="Cyan" )
plt.scatter(sorted_data, cdf, s=10, color="black")
plt.xlabel('AI Voice-Image Transcription Latency (s)', fontsize=60)
plt.ylabel('CDF', fontsize=60)
plt.tick_params(axis="both", labelsize="60")
plt.xlim(0, 17)
plt.ylim(0, 1)
plt.grid(True)

plt.subplots_adjust(left=.2,bottom=.2)
plt.legend(fontsize="50", loc="upper center")
plt.show()