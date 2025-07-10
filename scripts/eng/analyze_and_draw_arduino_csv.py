import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend

import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import os

# --- Parameters ---
CSV_FILENAME = 'triggers_arduino_better_500ms.csv'
SIGNAL_COLUMN = 0              # Index of the column to analyze
SAMPLING_RATE = 10000          # Hz (sampling rate used during acquisition)
MIN_DISTANCE_MS = 1.0          # Minimum distance between peaks (in ms)

def analyze_and_save_csv_plot(filename):
    try:
        data = np.loadtxt(filename, delimiter=',')

        print(f"--- CSV File Analysis: {filename} ---")
        print(f"Sampling rate used: {SAMPLING_RATE} Hz (threshold set at 50% of max amplitude)")

        # Handle 1D or 2D data
        if data.ndim == 1:
            signal = data
            print("The file contains a single column, it will be used.")
        else:
            signal = data[:, SIGNAL_COLUMN]
            print(f"The file contains {data.shape[1]} columns, using column {SIGNAL_COLUMN}.")

        signal_abs = np.abs(signal)
        threshold = 0.5 * np.max(signal_abs)
        print(f"Detection threshold (absolute): {threshold:.2f}")

        min_distance_samples = int(MIN_DISTANCE_MS * SAMPLING_RATE / 1000)
        print(f"Minimum distance between peaks: {MIN_DISTANCE_MS} ms")

        peak_indices, _ = find_peaks(signal_abs, height=threshold, distance=min_distance_samples)
        intervals_in_samples = np.diff(peak_indices)
        intervals_in_ms = (intervals_in_samples / SAMPLING_RATE) * 1000

        print("\n--- RESULTS ---")
        print(f"Number of detected peaks: {len(peak_indices)}")
        print(f"Total number of intervals: {len(intervals_in_ms)}")

        if len(intervals_in_ms) > 0:
            mean_interval = np.mean(intervals_in_ms)
            print(f"Mean interval: {mean_interval:.2f} ms")
            print(f"Min interval: {np.min(intervals_in_ms):.2f} ms")
            print(f"Max interval: {np.max(intervals_in_ms):.2f} ms")

            plt.figure(figsize=(12, 7))
            plt.hist(intervals_in_ms, bins=50, edgecolor='black', alpha=0.75)
            plt.axvline(mean_interval, color='red', linestyle='--', linewidth=2,
                        label=f'Mean = {mean_interval:.2f} ms')
            plt.title(f"Interval Distribution\nFile: {os.path.basename(filename)}", fontsize=16)
            plt.xlabel("Interval duration (ms)", fontsize=12)
            plt.ylabel("Number of intervals", fontsize=12)
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.6)

            output_dir = 'figures'
            os.makedirs(output_dir, exist_ok=True)
            base_name = os.path.splitext(os.path.basename(filename))[0]
            save_path = os.path.join(output_dir, f'distribution_intervals_{base_name}_csv.png')

            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()

            print(f"\nFigure successfully saved at: '{save_path}'")
        else:
            print("No interval to plot — figure was not created.")

    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    analyze_and_save_csv_plot(CSV_FILENAME)
