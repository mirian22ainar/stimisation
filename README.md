# 🧠 MEG Stimulus–Response Synchronization Project

Welcome to this repository dedicated to my final-year internship work at the NeuroSpin center (CEA Saclay), focused on improving the synchronization system used in magnetoencephalography (MEG) experiments. (In other words I'm working on optimizing the stimulation process in MEG experiments — which inspired the name Stimisation)

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

| File / Notebook                           | Description                                                                 |
|------------------------------------------|-----------------------------------------------------------------------------|
| [`protocole_etude_arduino.ipynb`](./protocole_etude_arduino.ipynb)          | Trigger generation using an Arduino microcontroller.                        |
| [`etude_photodiode.ipynb`](./etude_photodiode.ipynb)                        | Analysis of visual stimulus detection using a photodiode connected to an acquisition system. |
| [`fusion_arduino_photodiode.ipynb`](./fusion_arduino_photodiode.ipynb)     | Combined implementation: Arduino-based triggers + photodiode analysis.      |
| [`doc_meg.ipynb`](./doc_meg.ipynb)                                          | Educational documentation on signals exchanged during a MEG experiment: triggers, button responses, video, TTL, photodiode, etc. |
| [`README.md`](./README.md)                                                  | This file – project overview and repository navigation.                     |


⚠️ Some files are Jupyter Notebooks (`.ipynb`) while others are plain Markdown (`.md`). This allows for both **interactive execution** and **clear documentation**.

## 📌 Intended Audience

This repository is designed for:
- **Researchers or engineers** working with MEG systems who want to understand or adapt the signal exchange setup;
- **Students** in neuroscience or neuroengineering looking to get familiar with MEG synchronization mechanisms;
- Anyone interested in reproducing or improving a **modern, portable, and well-documented** trigger generation system.

## 📬 Contact

Feel free to contact me via GitHub or email if you have any questions or suggestions.

---

Thanks for your interest! ✨
