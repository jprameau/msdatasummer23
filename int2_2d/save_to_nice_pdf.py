import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def extract_experiment_name(file_name):
    parts = file_name.split('_')
    return parts[1] if len(parts) > 1 else None

def format_for_filename(title):
    return title.replace('$_', '').replace('^', '')

def plot_peaks_in_range(file_path, threshold, xmin, xmax, title):
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

    # Set up figure with inverted aspect ratio
    plt.figure(figsize=(plt.figaspect(np.sqrt(2))[1], plt.figaspect(np.sqrt(2))[0]))

    # Plot the data with continuous pink line
    plt.plot(x, y, 'm-', label='Data')  # Pink color for the plot
    plt.plot(x[peaks], y[peaks], 'co')  # Cyan color for the peaks as dots

    # Add x values above peaks
    for peak in peaks:
        if xmin <= x[peak] <= xmax:  # Check if x value is within specified range
            plt.text(x[peak], y[peak], f'{x[peak]:.4f}', ha='center', va='bottom', color='black', fontsize=8, fontname='Helvetica')

    # Extract experiment name from file name
    experiment_name = extract_experiment_name(file_path)

    # Set title and labels
    plt.title(rf'{title}', fontname='Helvetica', fontsize=12)  # Use LaTeX notation for formatting
    plt.xlabel("m/z", fontname='Helvetica')  # Label x-axis as "m/z"
    plt.ylabel("counts / a.u.", fontname='Helvetica')  # Label y-axis as "counts / a.u."

    # Hide the legend
    plt.legend().set_visible(False)

    # Convert title to lowercase and replace spaces with underscores for the PDF file name
    pdf_file_name = format_for_filename(title.lower()).replace(' ', '_') + '.pdf'

    # Save as PDF file
    plt.savefig(pdf_file_name, format='pdf', bbox_inches='tight')

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python3 scriptname.py <file_path> <threshold> <xmin> <xmax> <title>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    threshold = float(sys.argv[2])
    xmin = float(sys.argv[3])
    xmax = float(sys.argv[4])
    title = sys.argv[5]
    
    plot_peaks_in_range(file_path, threshold, xmin, xmax, title)

