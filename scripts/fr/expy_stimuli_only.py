from expyriment import design, control, stimuli, misc

# --- Setup Expyriment ---
exp = design.Experiment(name="Stimuli_Only")
control.set_develop_mode(True)
control.initialize(exp)

PERIOD = 250 # Intervalle total en ms
SQUARE_DURATION = 100  # ms

square = stimuli.Rectangle((400, 400), position=(0, 0))
blank = stimuli.BlankScreen()
square.preload()
blank.preload()

exp.add_data_variable_names(['trial', 'stimulus_time'])

control.start(skip_ready_screen=True)
clock2 = misc.Clock()
i = 1

while i <= 10000:
    while (clock2.time < i * PERIOD - 3):
        pass

    stim_time = clock2.time + square.present(update=True)

    while (clock2.time - stim_time < SQUARE_DURATION - 3):
        pass
    blank.present(update=True)

    exp.data.add([i, stim_time])
    i += 1
    exp.keyboard.process_control_keys()

control.end()
