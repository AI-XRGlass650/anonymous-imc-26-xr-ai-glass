import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Ossian Audio Inter-Packet Arrival Times.csv")
data1 = pd.read_csv("Meta Audio Inter-Packet Arrival Times.csv")

interval = data["Interval start"]
interval1 = data1["Interval start"]

packets = data["Packet Sizes"]
packets1 = data1["Packet Sizes"]

ossian_tests = []
meta_tests = []

ossian_times = []
meta_times = []

ossian_packets = []
meta_packets = []

o = 1
m = 1

past_time_ossian = None
past_time_meta = None

for i in range(len(interval)):
    if packets.iloc[i] > 0:
        ossian_packets.append(packets[i] / 8)
        if past_time_ossian is not None:
            ossian_time_difference = (interval.iloc[i] - past_time_ossian) * 1000
            if (ossian_time_difference < 400):
                ossian_times.append(ossian_time_difference)
            
                ossian_tests.append(o)
                o += 1
        past_time_ossian = interval[i]

for i in range(len(interval1)): 
    if packets1.iloc[i] > 0:
        meta_packets.append(packets1[i] / 8)
        if past_time_meta is not None:
            meta_time_difference = (interval1.iloc[i] - past_time_meta) * 1000
            if (meta_time_difference < 400):
                meta_times.append(meta_time_difference)
            
                meta_tests.append(m)
                m += 1
        past_time_meta = interval1[i]

sorted_data = np.sort(meta_times)
sorted_data1 = np.sort(ossian_times)

print(np.median(sorted_data), np.max(sorted_data), "\n")
print(np.median(sorted_data1), np.max(sorted_data1), "\n")

cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
cdf1 = np.arange(1, len(sorted_data1) + 1) / len(sorted_data1)

Meta_Glass = plt.plot(sorted_data1,  cdf1, linewidth=7, color="blue", label="RB-Meta")
Dragon_Glass = plt.plot(sorted_data,  cdf, linewidth=7, color="red", label="Dragon")
plt.xlabel('Inter-arrival Time (ms)', fontsize=60)
plt.ylabel('CDF', fontsize=60)
plt.xlim(0, 300)
plt.ylim(0, 1)
plt.tick_params(axis="both", labelsize="60")
plt.grid(True)
plt.legend(fontsize="50", loc="lower right")
plt.show()

sorted_packets = np.sort(meta_packets)
sorted_packets1 = np.sort(ossian_packets)

print(np.median(sorted_packets), np.max(sorted_packets), "\n")
print(np.median(sorted_packets1), np.max(sorted_packets1), "\n")

packets_cdf = np.arange(1, len(sorted_packets) + 1) / len(sorted_packets)
packets_cdf1 = np.arange(1, len(sorted_packets1) + 1) / len(sorted_packets1)

Meta_Glass = plt.plot(sorted_packets,  packets_cdf, linewidth=7, color="blue", label="RB-Meta")
Dragon_Glass = plt.plot(sorted_packets1,  packets_cdf1, linewidth=7, color="red", label="Dragon")
plt.xlabel('Packet Size (Bytes)', fontsize=60)
plt.ylabel('CDF', fontsize=60)
plt.xlim(0, 10000)
plt.ylim(0, 1)
plt.tick_params(axis="both", labelsize="60")
plt.grid(True)
plt.legend(fontsize="50", loc="lower right")
plt.show()