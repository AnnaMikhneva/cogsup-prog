from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE, C_WHITE, C_BLACK
import random

exp = design.Experiment(name="Ternus Illusion", background_colour=C_WHITE)
control.set_develop_mode()
control.initialize(exp)

def load(stims):
    for stim in stims:
        stim.preload()

def present_for(stims, frames=12):
    """Present stimuli for given number of frames using accurate timing."""
    t_ms = frames * (1000 / 60)  # More precise frame duration
    t0 = exp.clock.time
    
    # Draw stimuli once
    exp.screen.clear() 
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    
    # Wait for remaining time
    draw_time = exp.clock.time - t0
    exp.clock.wait(max(0, t_ms - draw_time))

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
    display_frames = 30  # Now actually ~500ms (30 frames at 60Hz)
    
    frame1 = [circles[0], circles[1], circles[2]]
    frame2 = [circles[1], circles[2], circles[3]]

    while True:
        present_for(frame1, frames=display_frames)

        if isi_frames > 0:
            exp.screen.clear()
            exp.screen.update()            
            exp.clock.wait(isi_frames * (1000 / 60))

        present_for(frame2, frames=display_frames)
 
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

# the second one does not really work on me but I feel like it could 