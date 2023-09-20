import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def extract_experiment_name(file_name):
    parts = file_name.split('_')
    return parts[1] if len(parts) > 1 else None

def plot_peaks_in_range(file_path, threshold, xmin, xmax):
    # Load the data
    data = np.loadtxt(file_path)

    # Extract x and y values within specified range
    x = data[:, 0]
    y = data[:, 1]
    mask = (x >= xmin) & (x <= xmax)
    x = x[mask]
    y = y[mask]

    # Find peaks
    peaks, _ = find_peaks(y, height=threshold)

    # Plot the data
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'm--', label='Data')  # Pink color for the plot
    plt.plot(x[peaks], y[peaks], 'co')  # Cyan color for the peaks as dots

    # Add x values above peaks
    for peak in peaks:
        if xmin <= x[peak] <= xmax:  # Check if x value is within specified range
            plt.text(x[peak], y[peak], f'{x[peak]:.4f}', ha='center', va='bottom', color='black', fontsize=8, fontname='Helvetica')

    # Extract experiment name from file name
    experiment_name = extract_experiment_name(file_path)

    # Set title and labels
    plt.title(f"{experiment_name} region 1", fontname='Helvetica')
    plt.xlabel("m/z", fontname='Helvetica')  # Label x-axis as "m/z"
    plt.ylabel("counts / a.u.", fontname='Helvetica')  # Label y-axis as "counts / a.u."

    # Add legend
    plt.legend()

    # Show the plot
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 scriptname.py <file_path> <threshold> <xmin> <xmax>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    threshold = float(sys.argv[2])
    xmin = float(sys.argv[3])
    xmax = float(sys.argv[4])
    
    plot_peaks_in_range(file_path, threshold, xmin, xmax)
