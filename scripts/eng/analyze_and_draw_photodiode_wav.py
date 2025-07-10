import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import find_peaks
import os

# --- Parameters ---
WAV_FILENAME = 'expy_stimuli_only_pc_gaming_250ms.wav'  # Name of the WAV file to analyze
MIN_INTERVAL_MS = 100.0  # Minimum interval between peaks (in ms)

def analyze_and_save_plot(filename):
    """
    Analyzes a photodiode signal in WAV format:
    - peak detection
    - interval calculation
    - interval histogram
    - plot of the signal with peaks
    """
    try:
        sampling_rate, data = wavfile.read(filename)
        print(f"\n--- Analyzing file: {filename} ---")
        print(f"Sampling rate: {sampling_rate} Hz")

        if data.ndim > 1:
            data = data[:, 0]  # Use only the first channel if stereo

        signal_abs = np.abs(data)
        threshold = 0.8 * np.max(signal_abs)
        print(f"Detection threshold (80% of max amplitude): {int(threshold)}")

        min_distance_samples = int(MIN_INTERVAL_MS * sampling_rate / 1000)

        peak_indices, _ = find_peaks(signal_abs, height=threshold, distance=min_distance_samples)
        intervals_in_samples = np.diff(peak_indices)
        intervals_in_ms = (intervals_in_samples / sampling_rate) * 1000

        print(f"\nNumber of detected peaks: {len(peak_indices)}")
        print(f"Number of intervals: {len(intervals_in_ms)}")

        if len(intervals_in_ms) > 0:
            mean_interval = np.mean(intervals_in_ms)
            print(f"Mean interval: {mean_interval:.2f} ms")
            print(f"Min: {np.min(intervals_in_ms):.2f} ms")
            print(f"Max: {np.max(intervals_in_ms):.2f} ms")

            # --- Histogram of intervals ---
            plt.figure(figsize=(12, 6))
            plt.hist(intervals_in_ms, bins=50, edgecolor='black', alpha=0.75)
            plt.axvline(mean_interval, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_interval:.2f} ms')
            plt.title(f"Interval Distribution — {os.path.basename(filename)}", fontsize=14)
            plt.xlabel("Interval duration (ms)")
            plt.ylabel("Number of intervals")
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.6)

            output_dir = 'figures'
            os.makedirs(output_dir, exist_ok=True)
            base_name = os.path.splitext(os.path.basename(filename))[0]
            save_hist_path = os.path.join(output_dir, f'distribution_intervals_{base_name}.png')
            plt.savefig(save_hist_path, dpi=300, bbox_inches='tight')
            plt.close()
            print(f"\nHistogram saved: {save_hist_path}")

            # --- Signal plot with detected peaks ---
            plt.figure(figsize=(15, 5))
            plt.plot(data, label='Signal')
            plt.plot(peak_indices, data[peak_indices], 'rx', label='Detected Peaks')
            plt.title(f"Signal and Detected Peaks — {base_name}")
            plt.xlabel("Samples")
            plt.ylabel("Amplitude")
            plt.legend()
            save_signal_path = os.path.join(output_dir, f'signal_peaks_{base_name}.png')
            plt.savefig(save_signal_path, dpi=300, bbox_inches='tight')
            plt.close()
            print(f"Signal plot saved: {save_signal_path}")

        else:
            print("No intervals detected — no figures generated.")

    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Auto-run ---
if __name__ == '__main__':
    analyze_and_save_plot(WAV_FILENAME)
