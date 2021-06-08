import sys
import matplotlib.pyplot as plt
import numpy as np


#receive input
input_files = sys.argv[1:-3]
output_file = sys.argv[-3]
x_label = sys.argv[-2]
y_label = sys.argv[-1]

#plot csv dat and find common x-axis range between them
plt.figure(figsize=(12,5))

list_ranges = []

for file in input_files:
    data = np.loadtxt(file, delimiter=',')
    left_val = np.min(data[:,0])
    right_val = np.max(data[:,0])
    range_val = (left_val, right_val)
    list_ranges.append(range_val)
    data_label = file[:-4]
    plt.plot(data[:,0], data[:,1], label=data_label)

plt.yscale('log')
plt.legend()
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.savefig(output_file)
plt.show()

max_left = max(list_ranges, key = lambda x: x[0])[0]
min_right = min(list_ranges, key = lambda x: x[1])[1]

print("Overlap range: ", (max_left, min_right))







