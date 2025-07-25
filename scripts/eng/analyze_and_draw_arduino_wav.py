import numpy as np
import matplotlib
# Specify the non-interactive backend 'Agg' BEFORE importing pyplot
# This prevents Matplotlib from trying to access a display server (like X11), which would crash in headless mode.
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import find_peaks
import os

# --- Parameters ---
WAV_FILENAME = 'triggers_arduino_better_250ms_100kHz.wav'
MIN_DISTANCE_MS = 100.0

def analyze_and_save_plot(filename):
    """
    Analyzes a WAV file to detect triggers, computes the intervals between them,
    generates a histogram of their distribution, and saves it as an image.
    """
    try:
        sampling_rate, data = wavfile.read(filename)
        print(f"--- Analyzing file: {filename} ---")
        print(f"Sampling rate read from file: {sampling_rate} Hz")

        if data.ndim > 1:
            data = data[:, 0]  # Take only one channel if stereo

        abs_signal = np.abs(data)
        threshold = 0.5 * np.max(abs_signal)
        print(f"Detection threshold (absolute): {int(threshold)} (computed at 50% of max amplitude)")

        min_distance_samples = int(MIN_DISTANCE_MS * sampling_rate / 1000)
        print(f"Minimum distance between peaks: {MIN_DISTANCE_MS} ms")
        
        peak_indices, _ = find_peaks(abs_signal, height=threshold, distance=min_distance_samples)
        interval_samples = np.diff(peak_indices)
        interval_ms = (interval_samples / sampling_rate) * 1000

        print("\n--- RESULTS ---")
        print(f"Number of peaks (triggers) detected: {len(peak_indices)}")
        print(f"Total number of intervals: {len(interval_ms)}")
        
        if len(interval_ms) > 0:
            mean_interval = np.mean(interval_ms)
            print(f"Mean interval: {mean_interval:.2f} ms")
            print(f"Minimum interval: {np.min(interval_ms):.2f} ms")
            print(f"Maximum interval: {np.max(interval_ms):.2f} ms")
        
            plt.figure(figsize=(12, 7))
            plt.hist(interval_ms, bins=50, edgecolor='black', alpha=0.75)
            plt.axvline(mean_interval, color='red', linestyle='--', linewidth=2, 
                        label=f'Mean = {mean_interval:.2f} ms')
            plt.title(f"Interval Duration Distribution\nFile: {os.path.basename(filename)}", fontsize=16)
            plt.xlabel("Interval Duration (ms)", fontsize=12)
            plt.ylabel("Number of Intervals (Frequency)", fontsize=12)
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.6)
            
            output_dir = 'figures'
            os.makedirs(output_dir, exist_ok=True)
            base_name = os.path.splitext(os.path.basename(filename))[0]
            save_path = os.path.join(output_dir, f'distribution_intervals_{base_name}_wav.png')
            
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
            
            print(f"\nFigure successfully saved to: '{save_path}'")
        else:
            print("No intervals to plot, figure was not created.")

    except FileNotFoundError:
        print(f"ERROR: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    analyze_and_save_plot(WAV_FILENAME)
