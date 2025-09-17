from expyriment import design, control, stimuli

# Create an experiment object
exp = design.Experiment(name="Two Squares")

# Initialize the experiment
control.initialize(exp)

# Create the red square (left)
red_square = stimuli.Rectangle(size=(50, 50), colour=(255, 0, 0))  # Red color

# Create the green square (right)
green_square = stimuli.Rectangle(size=(50, 50), colour=(0, 255, 0))  # Green color

# Set positions for the squares
# They should be separated by 200 pixels and centered as a whole
# So each square is offset by 100 pixels from center (50 + 50 = 100)
red_square.position = (-100, 0)    # Left square: 100 pixels left of center
green_square.position = (100, 0)   # Right square: 100 pixels right of center

# Start running the experiment
control.start(subject_id=1)

# Present both squares
red_square.present(clear=True, update=False)      # Present red square without clearing
green_square.present(clear=False, update=True)  # Present green square and update display

# Leave them on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()