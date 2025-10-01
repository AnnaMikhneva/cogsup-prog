from expyriment import design, control, stimuli


exp = design.Experiment(name="Triggering Effect with Different Speeds")


control.initialize(exp)


red_square = stimuli.Rectangle(size=(50, 50), colour=(255, 0, 0))  

green_square = stimuli.Rectangle(size=(50, 50), colour=(0, 255, 0))  


red_square.position = (-400, 0)

green_square.position = (0, 0)

control.start(subject_id=1)


red_square.present(clear=True, update=False)
green_square.present(clear=False, update=True)
exp.clock.wait(1000)  


red_speed = 7  
green_speed = red_speed * 3  
distance_to_cover = 350  
red_frames_to_move = distance_to_cover // red_speed  
green_frames_to_move = distance_to_cover // green_speed  


for frame in range(red_frames_to_move):
    red_square.move((red_speed, 0))  
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(1)  


for frame in range(green_frames_to_move):
    green_square.move((green_speed, 0))  
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(1) 


exp.clock.wait(1000)

control.end()

# No,  this does not look like a collision no more.