from expyriment import design, control, stimuli

# Create an experiment object
exp = design.Experiment(name="Triggering Effect with Different Speeds")

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
red_speed = 7  # Pixels per frame for red square
green_speed = red_speed * 3  # Green square moves 3 times faster than red square
distance_to_cover = 350  # Distance from red square's start to center
red_frames_to_move = distance_to_cover // red_speed  # Calculate frames needed for red square
green_frames_to_move = distance_to_cover // green_speed  # Calculate frames needed for green square

# Animate red square moving to the right until it reaches the green square
for frame in range(red_frames_to_move):
    red_square.move((red_speed, 0))  # Move right by red_speed pixels
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(1)  # Wait 1ms to control animation speed

# Once red square reaches green square, animate green square moving to the right at 3x speed
for frame in range(green_frames_to_move):
    green_square.move((green_speed, 0))  # Move right by green_speed pixels (3x faster)
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(1)  # Wait 1ms to control animation speed

# Show final display for 1 second
exp.clock.wait(1000)

# End the current session and quit expyriment
control.end()