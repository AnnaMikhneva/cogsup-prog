from expyriment import design, control, stimuli

def display_launching_event(exp, temporal_gap=0, spatial_gap=0, speed_ratio=1):
    """
    Display a horizontal launching event with customizable parameters.
    
    Parameters:
    exp: The experiment object
    temporal_gap: Delay in milliseconds between collision and movement of second square
    spatial_gap: Gap in pixels between the two squares at collision
    speed_ratio: Ratio of second square's speed to first square's speed (1 = same speed)
    """
    
    
    red_square = stimuli.Rectangle(size=(50, 50), colour=(255, 0, 0))  

    green_square = stimuli.Rectangle(size=(50, 50), colour=(0, 255, 0))  

    red_square.position = (-400, 0)  
    green_square.position = (spatial_gap, 0)

    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(1000)  

    red_speed = 7 
    green_speed = red_speed * speed_ratio  
    
    distance_to_cover = 350 - spatial_gap
    
    red_frames_to_move = int(distance_to_cover // red_speed)
    green_frames_to_move = int(distance_to_cover // green_speed)

    for frame in range(red_frames_to_move):
        red_square.move((red_speed, 0)) 
        red_square.present(clear=True, update=False)
        green_square.present(clear=False, update=True)
        exp.clock.wait(1)

    if temporal_gap > 0:
        exp.clock.wait(temporal_gap)

    for frame in range(green_frames_to_move):
        green_square.move((green_speed, 0)) 
        red_square.present(clear=True, update=False)
        green_square.present(clear=False, update=True)
        exp.clock.wait(1) 


    exp.clock.wait(1000)


exp = design.Experiment(name="Launching Events Comparison")


control.initialize(exp)

control.start(subject_id=1)


instructions = stimuli.TextScreen("Launching Events", 
    "You will see four different launching events:\n\n"
    "1. Standard Michottean launching\n"
    "2. Launching with temporal gap\n"
    "3. Launching with spatial gap\n"
    "4. Triggering (different speeds)\n\n"
    "Press any key to begin.")
instructions.present()
exp.keyboard.wait()

display_launching_event(exp, temporal_gap=0, spatial_gap=0, speed_ratio=1)

exp.clock.wait(500)


display_launching_event(exp, temporal_gap=200, spatial_gap=0, speed_ratio=1)

exp.clock.wait(500)


display_launching_event(exp, temporal_gap=0, spatial_gap=100, speed_ratio=1)


exp.clock.wait(500)


display_launching_event(exp, temporal_gap=0, spatial_gap=0, speed_ratio=3)


exp.keyboard.wait()

control.end()