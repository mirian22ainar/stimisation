import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import find_peaks
import os

# === Paramètres ===
NOM_FICHIER_WAV = 'arduino_trigger_master_timer_500ms_both_2.wav'
DISTANCE_MIN_MS = 100.0

def analyser_signaux_wav(nom_fichier):
    try:
        sampling_rate, data = wavfile.read(nom_fichier)
        if data.ndim != 2 or data.shape[1] < 2:
            raise ValueError("Le fichier WAV doit avoir au moins 2 canaux (Arduino, Photodiode).")

        ttl = data[:, 0]
        photodiode = data[:, 1]

        print(f"--- Analyse du fichier : {nom_fichier} ---")
        print(f"Taux d'échantillonnage : {sampling_rate} Hz")

        # Seuils dynamiques, photodiode basée sur l'amplitude absolue
        seuil_ttl = 0.5 * np.max(ttl)
        signal_photo_abs = np.abs(photodiode)
        seuil_photo = 0.8 * np.max(signal_photo_abs)
        print(f"Seuil TTL : {seuil_ttl:.2f}, Seuil Photodiode : {seuil_photo:.2f}")

        min_distance_samples = int((DISTANCE_MIN_MS / 1000) * sampling_rate)

        # Détection des pics
        ttl_peaks, _ = find_peaks(ttl, height=seuil_ttl, distance=min_distance_samples)
        photo_peaks, _ = find_peaks(signal_photo_abs, height=seuil_photo, distance=min_distance_samples)

        def analyse_intervalles(peaks, label):
            intervalles = np.diff(peaks) / sampling_rate * 1000  # ms
            moyenne = np.mean(intervalles)
            print(f"\n--- {label} ---")
            print(f"Nombre de triggers : {len(peaks)}")
            print(f"Intervalle moyen : {moyenne:.2f} ms")
            print(f"Min : {np.min(intervalles):.2f}, Max : {np.max(intervalles):.2f}, Écart-type : {np.std(intervalles):.2f}")

            plt.figure(figsize=(10, 5))
            plt.hist(intervalles, bins=40, edgecolor='black', alpha=0.8)
            plt.axvline(moyenne, color='red', linestyle='--', label=f'Moyenne = {moyenne:.2f} ms')
            plt.title(f'Intervalles entre triggers - {label}')
            plt.xlabel("Durée (ms)")
            plt.ylabel("Occurrences")
            plt.legend()
            os.makedirs('figures', exist_ok=True)
            plt.savefig(f'figures/hist_intervalles_{label.lower().replace(" ", "_")}.png')
            plt.close()

        analyse_intervalles(ttl_peaks, "Arduino")
        analyse_intervalles(photo_peaks, "Photodiode")

        # Délai Arduino → Photodiode
        matched_delays = []
        for t in ttl_peaks:
            deltas = photo_peaks - t
            pos_deltas = deltas[deltas > 0]
            if len(pos_deltas) > 0:
                delay = pos_deltas[0] / sampling_rate * 1000
                matched_delays.append(delay)

        matched_delays = np.array(matched_delays)
        print("\n--- Délai entre trigger Arduino et détection visuelle ---")
        print(f"Nombre d'appariements : {len(matched_delays)}")
        print(f"Délai moyen : {np.mean(matched_delays):.2f} ms, Min : {np.min(matched_delays):.2f}, Max : {np.max(matched_delays):.2f}, Jitter : {np.std(matched_delays):.2f} ms")

        plt.figure(figsize=(10, 5))
        plt.hist(matched_delays, bins=30, edgecolor='black', alpha=0.8)
        plt.axvline(np.mean(matched_delays), color='red', linestyle='--', label=f'Moyenne = {np.mean(matched_delays):.2f} ms')
        plt.title("Délai entre trigger Arduino et photodiode")
        plt.xlabel("Délai (ms)")
        plt.ylabel("Occurrences")
        plt.legend()
        plt.savefig('figures/delai_arduino_vs_photodiode.png')
        plt.close()

    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == '__main__':
    analyser_signaux_wav(NOM_FICHIER_WAV)
