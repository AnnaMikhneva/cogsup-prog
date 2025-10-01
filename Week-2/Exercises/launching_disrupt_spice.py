from expyriment import design, control, stimuli


exp = design.Experiment(name="Launching Effect with Spatial Gap")


control.initialize(exp)

red_square = stimuli.Rectangle(size=(50, 50), colour=(255, 0, 0)) 


green_square = stimuli.Rectangle(size=(50, 50), colour=(0, 255, 0)) 


red_square.position = (-400, 0)

#spatial_gap = 100
#spatial_gap = 50
spatial_gap = 45 # this is the smallest amount of space that still allows to feel that there is causality (at least in my perception)
green_square.position = (0, 0)  


control.start(subject_id=1)

red_square.present(clear=True, update=False)
green_square.present(clear=False, update=True)
exp.clock.wait(1000) 

speed = 7  
distance_to_cover = 350 - spatial_gap 
frames_to_move = int(distance_to_cover // speed)  


for frame in range(frames_to_move):
    red_square.move((speed, 0))  
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(1) 

for frame in range(frames_to_move):
    green_square.move((speed, 0))  
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(1)  


exp.clock.wait(1000)


control.end()