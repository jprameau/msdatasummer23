import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def extract_experiment_name(file_name):
    parts = file_name.split('_')
    return parts[1] if len(parts) > 1 else None

def plot_peaks_with_labels(file_path, threshold):
    # Load the data
    data = np.loadtxt(file_path)

    # Extract x and y values
    x = data[:, 0]
    y = data[:, 1]

    # Find peaks
    peaks, _ = find_peaks(y, height=threshold)

    # Plot the data
    plt.plot(x, y, 'r--')
    plt.plot(x[peaks], y[peaks], 'bo')  # Plot peaks as blue dots

    # Add x values above peaks
    for peak in peaks:
        if plt.xlim()[0] <= x[peak] <= plt.xlim()[1]:  # Check if x value is within current view
            plt.text(x[peak], y[peak], f'{x[peak]:.4f}', ha='center', va='bottom', color='black', fontsize=8)


    # Extract experiment name from file name
    experiment_name = extract_experiment_name(file_path)

    # Set title and labels
    plt.title(f"{experiment_name} region 1")
    plt.xlabel("x")
    plt.ylabel("y")

    # Show the plot
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 general_script.py <file_path> <threshold>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    threshold = float(sys.argv[2])
    
    plot_peaks_with_labels(file_path, threshold)
