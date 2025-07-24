from expyriment import design, control, stimuli, misc
import serial

# === Paramètres ===
SERIAL_PORT = '/dev/ttyACM0'  # À adapter si nécessaire
BAUDRATE = 115200
SQUARE_DURATION = 100  # Durée en ms du carré blanc

# === Initialisation Arduino & Expyriment ===
arduino = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=0.1)

exp = design.Experiment(name="Square Display on Serial Trigger")
control.set_develop_mode(True)
control.initialize(exp)

square = stimuli.Rectangle((400, 400))
blank = stimuli.BlankScreen()
square.preload()
blank.preload()

control.start(skip_ready_screen=True)

clock = misc.Clock()
print("✅ Prêt. Attente des commandes série 'SHOW'...")

try:
    while True:
        if arduino.in_waiting:
            line = arduino.readline().decode(errors="ignore").strip()
            if line == "SHOW":
                square.present(update=True)
                clock.wait(SQUARE_DURATION)
                blank.present(update=True)
        exp.keyboard.process_control_keys()
except KeyboardInterrupt:
    print("🛑 Interrompu manuellement.")
finally:
    arduino.close()
    control.end()
