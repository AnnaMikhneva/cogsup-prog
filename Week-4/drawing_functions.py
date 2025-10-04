from expyriment import design, control, stimuli
import random

def load(stims):
    """Preload the stimuli passed as input"""
    for stim in stims:
        stim.preload()

def timed_draw(stims):
    """Draw a list of (preloaded) stimuli on-screen, return the time it took to execute the drawing"""
    start_time = exp.clock.time
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    return exp.clock.time - start_time

def present_for(stims, t=1000):
    """Draw and keep stimuli on-screen for time t in ms (be mindful of edge cases!)"""
    # Clear the screen first
    exp.screen.clear()
    
    # Record start time
    start_time = exp.clock.time
    
    # Draw all stimuli
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    
    # Calculate remaining time after drawing
    draw_time = exp.clock.time - start_time
    remaining_time = t - draw_time
    
    # Present for the remaining duration
    if remaining_time > 0:
        exp.clock.wait(remaining_time)


""" Test functions """
exp = design.Experiment()

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
load([fixation])

n = 20
positions = [(random.randint(-300, 300), random.randint(-300, 300)) for _ in range(n)]
squares = [stimuli.Rectangle(size=(50, 50), position = pos) for pos in positions]
load(squares)

durations = []

t0 = exp.clock.time
for square in squares:
    if not square.is_preloaded:
        print("Preloading function not implemented correctly.")
    stims = [fixation, square] 
    present_for(stims, 500)
    t1 = exp.clock.time
    durations.append(t1-t0)
    t0 = t1

print(durations)

control.end()