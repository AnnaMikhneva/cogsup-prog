from expyriment import design, control, stimuli
import random
import math

def calculate_collision_point(green_square, red_square, direction):

    green_pos = green_square.position
    red_pos = red_square.position
    
    # Calculate the vector from green to red
    dx = red_pos[0] - green_pos[0]
    dy = red_pos[1] - green_pos[1]
    
    # Calculate distance between centers
    distance = math.sqrt(dx**2 + dy**2)
    
    # Calculate the point where the squares touch (considering their size)
    # Each square is 50x50, so the distance between centers at collision should be 50 pixels
    collision_ratio = 50 / distance if distance > 0 else 1
    

    collision_x = green_pos[0] + dx * collision_ratio
    collision_y = green_pos[1] + dy * collision_ratio
    
    return (collision_x, collision_y)


exp = design.Experiment(name="Random Motion Launching Events")

control.initialize(exp)

control.start(subject_id=1)

instructions = stimuli.TextScreen("Random Motion Launching", 
    "You will see three launching events with random directions.\n\n"
    "The green square will move toward the red square and launch it.\n\n"
    "Press any key to begin.")
instructions.present()
exp.keyboard.wait()

# Run three consecutive events
for event_num in range(3):
   
    green_square = stimuli.Rectangle(size=(50, 50), colour=(0, 255, 0))  
    red_square = stimuli.Rectangle(size=(50, 50), colour=(255, 0, 0))    
    
    green_square.position = (0, 0)
    
    angle = random.uniform(0, 2 * math.pi)
    red_x = 300 * math.cos(angle)
    red_y = 300 * math.sin(angle)
    red_square.position = (red_x, red_y)
    
    green_square.present(clear=True, update=False)
    red_square.present(clear=False, update=True)
    exp.clock.wait(1000)
    
    # Calculate direction vector from green to red
    dx = red_x - 0  
    dy = red_y - 0  
    distance = math.sqrt(dx**2 + dy**2)
    
    # Normalize direction vector
    if distance > 0:
        dx /= distance
        dy /= distance
    
    speed = 5 
    frames_to_move = int(distance // speed) - 10  # Subtract 10 to account for square size
    

    for frame in range(frames_to_move):
        green_square.move((dx * speed, dy * speed))
        green_square.present(clear=True, update=False)
        red_square.present(clear=False, update=True)
        exp.clock.wait(1)
        
        # Check for collision
        overlapping, overlap = green_square.overlapping_with_stimulus(red_square)
        if overlapping:
            break
    
    for frame in range(frames_to_move):
        red_square.move((dx * speed, dy * speed))
        green_square.present(clear=True, update=False)
        red_square.present(clear=False, update=True)
        exp.clock.wait(1)
    

    exp.clock.wait(1000)
    
    # Brief pause between events
    if event_num < 2:
        exp.clock.wait(500)



control.end()