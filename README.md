# 🧠 MEG Stimulus–Response Synchronization Project

Welcome to this repository dedicated to my final-year internship work at the NeuroSpin center (CEA Saclay), focused on improving the synchronization system used in magnetoencephalography (MEG) experiments. (In other words I'm working on optimizing the stimulation process in MEG experiments — which inspired the name *Stimisation*)

## 👩🏽 About Me

My name is Mirian. I'm a final-year engineering student at CentraleSupélec and ESME, specializing in medical robotics and biomedical technologies. This project is part of my internship within the MEG team at NeuroSpin.

## 🎯 Project Objective

The main goal of this work is to propose a **portable and modern alternative** to the current trigger generation and response capture system used in MEG experiments. The existing setup relies heavily on **parallel ports** or proprietary hardware.

My work focuses on:
- Generating triggers using an **Arduino microcontroller**;
- Studying the detection of visual stimuli displayed on screen using a **photodiode**;
- Combining both approaches into a unified and functional system;
- Clearly documenting the **signal circuits** involved in MEG experiments to assist future users.

## 📁 Repository Structure

| File / Notebook                                                                 | Description                                                                 |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [`protocole_study_arduino.ipynb`](./protocols_eng/protocole_study_arduino.ipynb) | Trigger generation using an Arduino microcontroller.                        |
| [`protocole_study_photodiode.ipynb`](./protocols_eng/protocole_study_photodiode.ipynb) | Protocol to evaluate the temporal precision of a photodiode when detecting LED flashes driven by Arduino. |
| [`protocole_study_photodiode_screen.ipynb`](./protocols_eng/protocole_study_photodiode_screen.ipynb) | Analysis of photodiode response to visual stimuli displayed on a computer screen. |
| [`protocole_study_sync_arduino_and_photodiode.ipynb`](./protocols_eng/protocole_study_sync_arduino_and_photodiode.ipynb) | **Trigger - visual stimuli synchronization measures**                           |
| [`meg_doc.ipynb`](./protocols_eng/meg_doc.ipynb)                                 | Educational documentation on signal exchange in MEG experiments.            |
| [`README.md`](./README.md)                                                      | This file – project overview and repository navigation.                     |


⚠️ Some files are Jupyter Notebooks (`.ipynb`) while others are plain Markdown (`.md`). This allows for both **interactive execution** and **clear documentation**.

## 📌 Intended Audience

This repository is designed for:
- **Researchers or engineers** working with MEG systems who want to understand or adapt the signal exchange setup;
- **Students** in neuroscience or neuroengineering looking to get familiar with MEG synchronization mechanisms;
- Anyone interested in reproducing or improving a **modern, portable, and well-documented** trigger generation system.

## 📬 Contact

Feel free to contact me via GitHub or email if you have any questions or suggestions.

Thanks for your interest! ✨

---

# 🧠 Projet de Synchronisation Stimuli–Réponses en MEG

Bienvenue dans ce dépôt dédié à mon travail de stage de fin d'études, réalisé au sein du centre NeuroSpin (CEA Saclay), portant sur l'amélioration du système de synchronisation utilisé lors des expériences de magnétoencéphalographie (MEG).  
(Autrement dit, je travaille sur l’**optimisation du processus de stimulation** dans les expériences MEG — d'où le nom *Stimisation*.)

## 👩🏽 À propos de moi

Je m'appelle Mirian. Je suis étudiante en dernière année d’école d’ingénieur à CentraleSupélec et à l’ESME, spécialisée en robotique médicale et technologies biomédicales.  
Ce projet s’inscrit dans le cadre de mon stage, réalisé au sein de l’équipe MEG à NeuroSpin.

## 🎯 Objectif du projet

L’objectif principal de ce travail est de proposer une **alternative portable et moderne** au système actuel de génération de triggers et de capture des réponses utilisé en MEG.  
Le système existant repose fortement sur des **ports parallèles** ou du matériel propriétaire.

Mon travail consiste à :
- Générer des triggers à l’aide d’un **microcontrôleur Arduino** ;
- Étudier la détection des stimuli visuels affichés à l’écran à l’aide d’une **photodiode** ;
- Combiner ces deux approches dans un système unifié et fonctionnel ;
- Documenter clairement les **circuits de signaux** utilisés dans les expériences MEG afin d’en faciliter la compréhension et la réutilisation.

## 📁 Structure du dépôt

| Fichier / Notebook                                                              | Description                                                                 |
|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [`protocole_etude_arduino.ipynb`](./protocoles_fr/protocole_etude_arduino.ipynb) | Génération de triggers avec un microcontrôleur Arduino.                     |
| [`protocole_etude_photodiode.ipynb`](./protocoles_fr/protocole_etude_photodiode.ipynb) | Protocole d’évaluation de la précision temporelle d’une photodiode lors de la détection d’éclairs LED pilotés par Arduino. |
| [`protocole_etude_photodiode_screen.ipynb`](./protocoles_fr/protocole_etude_photodiode_screen.ipynb) | Analyse de la réponse d’une photodiode à des stimuli visuels affichés sur un écran d’ordinateur. |
| [`protocole_etude_sync_arduino_et_photodiode.ipynb`](./protocoles_fr/protocole_etude_sync_arduino_et_photodiode.ipynb) | Implémentation combinée : Arduino + photodiode.                             |
| [`meg_doc.ipynb`](./protocoles_fr/meg_doc.ipynb)                                 | Documentation pédagogique sur les échanges de signaux en expérience MEG.    |
| [`README.md`](./README.md)                                                      | Ce fichier – aperçu du projet et navigation dans le dépôt.                  |



⚠️ Certains fichiers sont des notebooks Jupyter (`.ipynb`) tandis que d’autres sont en Markdown (`.md`), ce qui permet à la fois une **exécution interactive** et une **documentation claire**.

## 📌 Public cible

Ce dépôt s’adresse à :
- Des **chercheurs ou ingénieurs** travaillant sur des systèmes MEG souhaitant comprendre ou adapter le câblage et l’échange de signaux ;
- Des **étudiants** en neurosciences ou en neuro-ingénierie souhaitant se familiariser avec les mécanismes de synchronisation en MEG ;
- Toute personne souhaitant reproduire ou améliorer un système de génération de triggers **moderne, portable et bien documenté**.

## 📬 Contact

N’hésitez pas à me contacter via GitHub ou par e-mail si vous avez des questions ou suggestions.

Merci pour votre intérêt ! ✨
