from expyriment import design, control, stimuli

# Create an experiment object
exp = design.Experiment(name="Launching Effect with Temporal Delay")

# Initialize the experiment
control.initialize(exp)

# Create the red square (will start on the left)
red_square = stimuli.Rectangle(size=(50, 50), colour=(255, 0, 0))  # Red color

# Create the green square (will start at the center)
green_square = stimuli.Rectangle(size=(50, 50), colour=(0, 255, 0))  # Green color

# Set initial positions as specified
# Red square starts 400 pixels left from center
red_square.position = (-400, 0)
# Green square starts at center
green_square.position = (0, 0)

# Start running the experiment
control.start(subject_id=1)

# Present both squares side by side for 1 second
red_square.present(clear=True, update=False)
green_square.present(clear=False, update=True)
exp.clock.wait(1000)  # Wait for 1 second

# Define animation parameters
speed = 7  # Pixels per frame (adjust to match video speed)
distance_to_cover = 350  # Distance from red square's start to center
frames_to_move = distance_to_cover // speed  # Calculate frames needed

# Animate red square moving to the right until it reaches the green square
for frame in range(frames_to_move):
    red_square.move((speed, 0))  # Move right by speed pixels
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(1)  # Wait 1ms to control animation speed

# Introduce a temporal delay between collision and green square movement
# Start with a long delay (2000ms = 2 seconds) to see how it disrupts causality
#delay_duration = 2000 
#delay_duration = 1000 
#delay_duration = 500 
#delay_duration = 300
delay_duration = 100   
exp.clock.wait(delay_duration)

# After the delay, animate green square moving to the right
for frame in range(frames_to_move):
    green_square.move((speed, 0))  # Move right by speed pixels
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(1)  # Wait 1ms to control animation speed

# Show final display for 1 second
exp.clock.wait(1000)

# End the current session and quit expyriment
control.end()