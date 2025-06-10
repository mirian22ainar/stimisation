from serial import Serial
import time

arduino = Serial('/dev/ttyACM0', 115200)
time.sleep(2)  # Laisse le temps à l'Arduino de redémarrer

# Optionnel : envoyer un signal pour débuter
arduino.write(b'START')  # À adapter si tu fais un mode déclenchement côté Arduino
