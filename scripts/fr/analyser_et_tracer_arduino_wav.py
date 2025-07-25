import numpy as np
import matplotlib
# Spécifier le backend non-interactif 'Agg' AVANT d'importer pyplot
# Ceci empêche Matplotlib de chercher un serveur d'affichage (X11) et de crasher.
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import find_peaks
import os

# --- Paramètres ---
NOM_FICHIER_WAV = 'triggers_arduino_better_250ms_100kHz.wav'
DISTANCE_MIN_MS = 100.0

def analyser_et_sauvegarder_graphique(nom_fichier):
    """
    Analyse un fichier WAV pour trouver les triggers, calcule les intervalles,
    génère un histogramme de leur distribution et le sauvegarde en image.
    """
    try:
        sampling_rate, data = wavfile.read(nom_fichier)
        print(f"--- Analyse du fichier : {nom_fichier} ---")
        print(f"Taux d'échantillonnage lu dans le fichier : {sampling_rate} Hz")

        if data.ndim > 1:
            data = data[:, 0]

        signal_abs = np.abs(data)
        seuil = 0.5 * np.max(signal_abs)
        print(f"Seuil de détection (absolu) : {int(seuil)} (calculé à 50% de l'amplitude max)")

        distance_min_samples = int(DISTANCE_MIN_MS * sampling_rate / 1000)
        print(f"Distance minimale entre pics : {DISTANCE_MIN_MS} ms")
        
        indices_pics, _ = find_peaks(signal_abs, height=seuil, distance=distance_min_samples)
        intervalles_en_samples = np.diff(indices_pics)
        intervalles_en_ms = (intervalles_en_samples / sampling_rate) * 1000

        print("\n--- RÉSULTATS ---")
        print(f"Nombre de pics (triggers) détectés : {len(indices_pics)}")
        print(f"Nombre total d'intervalles : {len(intervalles_en_ms)}")
        
        if len(intervalles_en_ms) > 0:
            moyenne = np.mean(intervalles_en_ms)
            print(f"Intervalle moyen : {moyenne:.2f} ms")
            print(f"Intervalle min : {np.min(intervalles_en_ms):.2f} ms")
            print(f"Intervalle max : {np.max(intervalles_en_ms):.2f} ms")
        
            plt.figure(figsize=(12, 7))
            plt.hist(intervalles_en_ms, bins=50, edgecolor='black', alpha=0.75)
            plt.axvline(moyenne, color='red', linestyle='--', linewidth=2, 
                        label=f'Moyenne = {moyenne:.2f} ms')
            plt.title(f"Distribution des durées d'intervalles\nFichier: {os.path.basename(nom_fichier)}", fontsize=16)
            plt.xlabel("Durée de l'intervalle (ms)", fontsize=12)
            plt.ylabel("Nombre d'intervalles (Fréquence)", fontsize=12)
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.6)
            
            output_dir = 'figures'
            os.makedirs(output_dir, exist_ok=True)
            base_name = os.path.splitext(os.path.basename(nom_fichier))[0]
            save_path = os.path.join(output_dir, f'distribution_intervalles_{base_name}_wav.png')
            
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
            
            print(f"\nFigure sauvegardée avec succès sous : '{save_path}'")
        else:
            print("Aucun intervalle à tracer, la figure n'a pas été créée.")

    except FileNotFoundError:
        print(f"ERREUR : Le fichier '{nom_fichier}' est introuvable.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == '__main__':
    analyser_et_sauvegarder_graphique(NOM_FICHIER_WAV)