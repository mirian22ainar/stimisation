import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import find_peaks
import os

# === Parameters ===
WAV_FILENAME = 'arduino_trigger_master_timer_500ms_both_2.wav'
MIN_DISTANCE_MS = 100.0

def analyze_wav_signals(filename):
    try:
        sampling_rate, data = wavfile.read(filename)
        if data.ndim != 2 or data.shape[1] < 2:
            raise ValueError("WAV file must contain at least 2 channels (Arduino, Photodiode).")

        ttl = data[:, 0]
        photodiode = data[:, 1]

        print(f"--- Analyzing file: {filename} ---")
        print(f"Sampling rate: {sampling_rate} Hz")

        # Dynamic thresholds, photodiode based on absolute amplitude
        ttl_threshold = 0.5 * np.max(ttl)
        photo_abs = np.abs(photodiode)
        photo_threshold = 0.8 * np.max(photo_abs)
        print(f"TTL threshold: {ttl_threshold:.2f}, Photodiode threshold: {photo_threshold:.2f}")

        min_distance_samples = int((MIN_DISTANCE_MS / 1000) * sampling_rate)

        # Peak detection
        ttl_peaks, _ = find_peaks(ttl, height=ttl_threshold, distance=min_distance_samples)
        photo_peaks, _ = find_peaks(photo_abs, height=photo_threshold, distance=min_distance_samples)

        def analyze_intervals(peaks, label):
            intervals = np.diff(peaks) / sampling_rate * 1000  # in ms
            mean_val = np.mean(intervals)
            print(f"\n--- {label} ---")
            print(f"Number of triggers: {len(peaks)}")
            print(f"Mean interval: {mean_val:.2f} ms")
            print(f"Min: {np.min(intervals):.2f}, Max: {np.max(intervals):.2f}, Std Dev: {np.std(intervals):.2f}")

            plt.figure(figsize=(10, 5))
            plt.hist(intervals, bins=40, edgecolor='black', alpha=0.8)
            plt.axvline(mean_val, color='red', linestyle='--', label=f'Mean = {mean_val:.2f} ms')
            plt.title(f'Trigger intervals - {label}')
            plt.xlabel("Duration (ms)")
            plt.ylabel("Occurrences")
            plt.legend()
            os.makedirs('figures', exist_ok=True)
            filename_safe = label.lower().replace(" ", "_")
            plt.savefig(f'figures/hist_intervals_{filename_safe}.png')
            plt.close()

        analyze_intervals(ttl_peaks, "Arduino")
        analyze_intervals(photo_peaks, "Photodiode")

        # Delay Arduino → Photodiode
        matched_delays = []
        for t in ttl_peaks:
            deltas = photo_peaks - t
            pos_deltas = deltas[deltas > 0]
            if len(pos_deltas) > 0:
                delay = pos_deltas[0] / sampling_rate * 1000
                matched_delays.append(delay)

        matched_delays = np.array(matched_delays)
        print("\n--- Delay between Arduino trigger and photodiode detection ---")
        print(f"Number of matched triggers: {len(matched_delays)}")
        print(f"Mean delay: {np.mean(matched_delays):.2f} ms, Min: {np.min(matched_delays):.2f}, Max: {np.max(matched_delays):.2f}, Jitter: {np.std(matched_delays):.2f} ms")

        plt.figure(figsize=(10, 5))
        plt.hist(matched_delays, bins=30, edgecolor='black', alpha=0.8)
        plt.axvline(np.mean(matched_delays), color='red', linestyle='--', label=f'Mean = {np.mean(matched_delays):.2f} ms')
        plt.title("Delay between Arduino trigger and photodiode detection")
        plt.xlabel("Delay (ms)")
        plt.ylabel("Occurrences")
        plt.legend()
        plt.savefig('figures/delay_arduino_vs_photodiode.png')
        plt.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    analyze_wav_signals(WAV_FILENAME)
