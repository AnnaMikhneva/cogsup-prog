from expyriment import design, control, stimuli

exp = design.Experiment(name="Launching Effect with Temporal Delay")

control.initialize(exp)

red_square = stimuli.Rectangle(size=(50, 50), colour=(255, 0, 0))  

green_square = stimuli.Rectangle(size=(50, 50), colour=(0, 255, 0))  


red_square.position = (-400, 0)

green_square.position = (0, 0)

control.start(subject_id=1)


red_square.present(clear=True, update=False)
green_square.present(clear=False, update=True)
exp.clock.wait(1000)  


speed = 7 
distance_to_cover = 350  
frames_to_move = distance_to_cover // speed 

for frame in range(frames_to_move):
    red_square.move((speed, 0))  
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(1)  


#delay_duration = 2000 
#delay_duration = 1000 
#delay_duration = 500 
#delay_duration = 300
delay_duration = 100   # this is the smallest amount of delay time that still allows to feel that there is causality 
exp.clock.wait(delay_duration)


for frame in range(frames_to_move):
    green_square.move((speed, 0))  
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(1)  
exp.clock.wait(1000)


control.end()