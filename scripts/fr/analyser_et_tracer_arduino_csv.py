import numpy as np
import matplotlib
matplotlib.use('Agg')  # Utilisation d'un backend non-interactif

import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import os

# --- Paramètres ---
NOM_FICHIER_CSV = 'triggers_arduino_better_500ms.csv'
COLONNE_SIGNAUX = 0           # index de la colonne à analyser
SAMPLING_RATE = 10000         # Hz (échantillonnage utilisé lors de l'acquisition)
DISTANCE_MIN_MS = 1.0         # Distance minimale entre deux pics (en ms)

def analyser_et_sauvegarder_graphique_csv(nom_fichier):
    try:
        data = np.loadtxt(nom_fichier, delimiter=',')

        print(f"--- Analyse du fichier CSV : {nom_fichier} ---")
        print(f"Taux d'échantillonnage utilisé : {SAMPLING_RATE} Hz (calculé à 50% de l'amplitude max)")

        # Gérer 1D ou 2D
        if data.ndim == 1:
            signal = data
            print("Le fichier contient une seule colonne, elle sera utilisée.")
        else:
            signal = data[:, COLONNE_SIGNAUX]
            print(f"Le fichier contient {data.shape[1]} colonnes, utilisation de la colonne {COLONNE_SIGNAUX}.")

        signal_abs = np.abs(signal)
        seuil = 0.5 * np.max(signal_abs)
        print(f"Seuil de détection (absolu) : {seuil:.2f}")

        distance_min_samples = int(DISTANCE_MIN_MS * SAMPLING_RATE / 1000)
        print(f"Distance minimale entre pics : {DISTANCE_MIN_MS} ms")

        indices_pics, _ = find_peaks(signal_abs, height=seuil, distance=distance_min_samples)
        intervalles_en_samples = np.diff(indices_pics)
        intervalles_en_ms = (intervalles_en_samples / SAMPLING_RATE) * 1000

        print("\n--- RÉSULTATS ---")
        print(f"Nombre de pics détectés : {len(indices_pics)}")
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
            plt.title(f"Distribution des intervalles\nFichier: {os.path.basename(nom_fichier)}", fontsize=16)
            plt.xlabel("Durée de l'intervalle (ms)", fontsize=12)
            plt.ylabel("Nombre d'intervalles", fontsize=12)
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.6)

            output_dir = 'figures'
            os.makedirs(output_dir, exist_ok=True)
            base_name = os.path.splitext(os.path.basename(nom_fichier))[0]
            save_path = os.path.join(output_dir, f'distribution_intervalles_{base_name}_csv.png')

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
    analyser_et_sauvegarder_graphique_csv(NOM_FICHIER_CSV)
