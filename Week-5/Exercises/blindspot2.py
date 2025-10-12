from expyriment import design, control, stimuli
from expyriment.misc.constants import (
    C_WHITE, C_BLACK,
    K_SPACE, K_UP, K_DOWN, K_LEFT, K_RIGHT,
    K_1, K_2, K_l, K_r
)

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10, colour=C_BLACK)
    c.preload()
    return c

def run_trial(side):

    if side == "left":
        cover_eye = "RIGHT"
        fixate_side = "LEFT"
        fixation_pos = [-300, 0]  
        start_pos = [300, 0]      
    elif side == "right":
        cover_eye = "LEFT"
        fixate_side = "RIGHT"
        fixation_pos = [300, 0]  
        start_pos = [-300, 0]     
    
    instructions = stimuli.TextScreen(
        "Blind Spot Test",
        f"Please cover your {cover_eye} eye.\n\n"
        f"Fixate on the {fixate_side} cross with your open eye.\n\n"
        "Use ARROW KEYS to move the circle.\n"
        "Press 1 to make SMALLER, 2 to make LARGER.\n\n"
        "Move the circle until it DISAPPEARS in your blind spot.\n"
        "Press SPACE when you can't see the circle anymore."
    )
    instructions.present()
    exp.keyboard.wait(K_SPACE)
    

    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=fixation_pos)
    fixation.preload()

    radius = 75
    position = list(start_pos)
    circle = make_circle(radius, position)

    while True:
        exp.screen.clear()
        fixation.present(clear=False, update=False)
        circle.present(clear=False, update=False)
        exp.screen.update()

        key = exp.keyboard.check()
        if key == K_SPACE:
            break
        elif key == K_UP:
            position[1] += 5
        elif key == K_DOWN:
            position[1] -= 5
        elif key == K_LEFT:
            position[0] -= 5
        elif key == K_RIGHT:
            position[0] += 5
        elif key == K_1:  
            radius = max(10, radius - 5)
        elif key == K_2: 
            radius = min(200, radius + 5)
        
        circle = make_circle(radius, position)

    exp.data.add([side, radius, position[0], position[1]])


control.start(subject_id=1)

eye_choice_screen = stimuli.TextScreen(
    "Blind Spot Test",
    "Which eye would you like to test?\n\n"
    "Press **L** to test your LEFT eye (cover RIGHT eye)\n"
    "Press **R** to test your RIGHT eye (cover LEFT eye)"
)
eye_choice_screen.present()
key = exp.keyboard.wait([K_l, K_r])

if key == K_l:
    side = "left"
else:
    side = "right"

run_trial(side)


finish_screen = stimuli.TextScreen(
    "Blind Spot Test",
    "Thank you for participating!\n\n"
    "Press any key to exit."
)
finish_screen.present()
exp.keyboard.wait()


control.end()
