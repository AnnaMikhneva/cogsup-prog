from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE, C_WHITE, C_BLACK
import random
from drawing_functions import load, present_for

exp = design.Experiment(name="Ternus Illusion", background_colour=C_WHITE)
control.set_develop_mode()
control.initialize(exp)



def make_circles(radius, positions, colors=None):
    circles = []
    for i, pos in enumerate(positions):
        c = stimuli.Circle(radius=radius, position=pos, colour=C_BLACK)

        if colors is not None:
            tag_pos = (radius * 0.6, 0) 
            tag = stimuli.Circle(radius=5, colour=colors[i], position=tag_pos)
            tag.plot(c)

        circles.append(c)

    load(circles)
    return circles

def run_trial(radius=30, isi_frames=1, color_tags=False):
    positions = [(-150,0), (-50,0), (50,0), (150,0)]
    tag_colors = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0)] if color_tags else None
    colors = [(255,0,0),    
          (0,0,255),   
          (0,255,0),   
          (255,255,0)]  

    circles = make_circles(radius, positions, colors=tag_colors)
    display_frames = 30  
    
    frame1 = [circles[0], circles[1], circles[2]]
    frame2 = [circles[1], circles[2], circles[3]]

    while True:
        present_for(exp, frame1, num_frames=display_frames)

        if isi_frames > 0:
            exp.screen.clear()
            exp.screen.update()            
            exp.clock.wait(isi_frames * (1000 / 60))

        present_for(exp, frame2, num_frames=display_frames)
  
        if isi_frames > 0:
            exp.screen.clear()
            exp.screen.update()
            exp.clock.wait(isi_frames * (1000 / 60))

        if exp.keyboard.check(K_SPACE):
            break


trials = [
    {"radius":30, "isi_frames":0, "color_tags":False},
    {"radius":30, "isi_frames":5, "color_tags":False},
    {"radius":30, "isi_frames":5, "color_tags":True}
]

control.start(subject_id=random.randint(1, 999))
for trial in trials:
    run_trial(**trial)
control.end()
