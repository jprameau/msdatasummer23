import numpy  as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

data = np.loadtxt('data_v2_acn_reg1.txt')


# Extract x and y values
x = data[:, 0]
y = data[:, 1]


# Find peaks
peaks, _ = find_peaks(y, height=20000)  # You may need to adjust the 'height' parameter

# Plot the data
plt.plot(x, y, 'r--')
plt.plot(x[peaks], y[peaks], 'bo')  # Plot peaks as blue dots


# Add x values above peaks
for peak in peaks:
    if plt.xlim()[0] <= x[peak] <= plt.xlim()[1]:  # Check if x value is within current view
        plt.text(x[peak], y[peak], f'{x[peak]:.2f}', ha='center', va='bottom', color='black', fontsize=8)


plt.plot(x, y,'r--')
plt.title("V2 region 1")
plt.xlabel("m/z")
plt.ylabel("counts")

plt.show()
