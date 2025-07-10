import numpy as np
import matplotlib
matplotlib.use('Agg')  # Backend non interactif
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import find_peaks
import os

# --- Paramètres ---
NOM_FICHIER_WAV = 'expy_stimuli_only_pc_gaming_250ms.wav'  # Nom du fichier WAV à analyser
DISTANCE_MIN_MS = 100.0                       # Intervalle minimal entre pics

def analyser_et_sauvegarder_graphique(nom_fichier):
    """
    Analyse un signal photodiode au format WAV :
    - détection des pics
    - calcul des intervalles
    - histogramme des intervalles
    - tracé du signal avec pics
    """
    try:
        sampling_rate, data = wavfile.read(nom_fichier)
        print(f"\n--- Analyse du fichier : {nom_fichier} ---")
        print(f"Taux d'échantillonnage : {sampling_rate} Hz")

        if data.ndim > 1:
            data = data[:, 0]

        signal_abs = np.abs(data)
        seuil = 0.8 * np.max(signal_abs)
        print(f"Seuil de détection (80% amplitude max) : {int(seuil)}")

        distance_min_samples = int(DISTANCE_MIN_MS * sampling_rate / 1000)

        indices_pics, _ = find_peaks(signal_abs, height=seuil, distance=distance_min_samples)
        intervalles_en_samples = np.diff(indices_pics)
        intervalles_en_ms = (intervalles_en_samples / sampling_rate) * 1000

        print(f"\nNombre de pics détectés : {len(indices_pics)}")
        print(f"Nombre d'intervalles : {len(intervalles_en_ms)}")

        if len(intervalles_en_ms) > 0:
            moyenne = np.mean(intervalles_en_ms)
            print(f"Intervalle moyen : {moyenne:.2f} ms")
            print(f"Min : {np.min(intervalles_en_ms):.2f} ms")
            print(f"Max : {np.max(intervalles_en_ms):.2f} ms")

            # --- Histogramme des intervalles ---
            plt.figure(figsize=(12, 6))
            plt.hist(intervalles_en_ms, bins=50, edgecolor='black', alpha=0.75)
            plt.axvline(moyenne, color='red', linestyle='--', linewidth=2, label=f'Moyenne = {moyenne:.2f} ms')
            plt.title(f"Distribution des intervalles — {os.path.basename(nom_fichier)}", fontsize=14)
            plt.xlabel("Durée de l'intervalle (ms)")
            plt.ylabel("Nombre d'intervalles")
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.6)

            output_dir = 'figures'
            os.makedirs(output_dir, exist_ok=True)
            base_name = os.path.splitext(os.path.basename(nom_fichier))[0]
            save_hist_path = os.path.join(output_dir, f'distribution_intervalles_{base_name}.png')
            plt.savefig(save_hist_path, dpi=300, bbox_inches='tight')
            plt.close()
            print(f"\nHistogramme sauvegardé : {save_hist_path}")

            # --- Tracé du signal avec pics ---
            plt.figure(figsize=(15, 5))
            plt.plot(data, label='Signal')
            plt.plot(indices_pics, data[indices_pics], 'rx', label='Pics détectés')
            plt.title(f"Signal et pics détectés — {base_name}")
            plt.xlabel("Échantillons")
            plt.ylabel("Amplitude")
            plt.legend()
            save_signal_path = os.path.join(output_dir, f'signal_pics_{base_name}.png')
            plt.savefig(save_signal_path, dpi=300, bbox_inches='tight')
            plt.close()
            print(f"Tracé du signal sauvegardé : {save_signal_path}")

        else:
            print("Aucun intervalle détecté — pas de figure générée.")

    except FileNotFoundError:
        print(f"ERREUR : Le fichier '{nom_fichier}' est introuvable.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# --- Lancement automatique ---
if __name__ == '__main__':
    analyser_et_sauvegarder_graphique(NOM_FICHIER_WAV)
