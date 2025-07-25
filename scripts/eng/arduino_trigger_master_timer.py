from expyriment import design, control, stimuli, misc
import serial

# === Parameters ===
SERIAL_PORT = '/dev/ttyACM0'  # Adjust if needed
BAUDRATE = 115200
SQUARE_DURATION = 100  # Duration of white square in ms

# === Initialize Arduino & Expyriment ===
arduino = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=0.1)

exp = design.Experiment(name="Square Display on Serial Trigger")
control.set_develop_mode(True)
control.initialize(exp)

square = stimuli.Rectangle((400, 400))  # White square
blank = stimuli.BlankScreen()
square.preload()
blank.preload()

control.start(skip_ready_screen=True)

clock = misc.Clock()
print("✅ Ready. Waiting for 'SHOW' serial commands...")

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
    print("🛑 Manually interrupted.")
finally:
    arduino.close()
    control.end()
