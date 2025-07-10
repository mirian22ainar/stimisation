from serial import Serial
import time

arduino = Serial('/dev/ttyACM0', 115200)
time.sleep(2)  # Give the Arduino time to reset after opening the connection

# Optional: send a signal to initiate communication
arduino.write(b'START')
