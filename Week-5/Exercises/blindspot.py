from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_SPACE, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_1, K_2

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10, colour=C_BLACK)
    c.preload()
    return c

""" Experiment """
def run_trial(side):
    # Determine instructions based on side
    if side == "left":
        cover_eye = "RIGHT"
        fixate_side = "LEFT"
        start_pos = (-300, 0)  
    else:  
        cover_eye = "LEFT"
        fixate_side = "RIGHT"
        start_pos = (300, 0)   
    
    # Show instructions
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
    
    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[300, 0] if side == "left" else [-300, 0])
    fixation.preload()

    radius = 75
    position = list(start_pos)
    circle = make_circle(radius, position)

    while True:
        # Present both stimuli
        exp.screen.clear()
        fixation.present(clear=False, update=False)
        circle.present(clear=False, update=False)
        exp.screen.update()
        
        # Handle keyboard input
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
        elif key == K_1:  # Smaller
            radius = max(10, radius - 5)
        elif key == K_2:  # Larger
            radius = min(200, radius + 5)
        
        # Update circle with new position and size
        circle = make_circle(radius, position)

control.start(subject_id=1)

# Get user input for which eye to test
eye_choice_screen = stimuli.TextScreen(
    "Blind Spot Test",
    "Which eye would you like to test first?\n\n"
    "Press 1 for LEFT eye (cover RIGHT eye)\n"
    "Press 2 for RIGHT eye (cover LEFT eye)"
)
eye_choice_screen.present()
key = exp.keyboard.wait([K_1, K_2])

if key == K_1:
    first_side = "left"
else:
    first_side = "right"

# Run first trial
run_trial(first_side)

other_eye_screen = stimuli.TextScreen(
    "Blind Spot Test",
    "Would you like to test the other eye?\n\n"
    "Press 1 for YES\n"
    "Press 2 for NO"
)
other_eye_screen.present()
key = exp.keyboard.wait([K_1, K_2])

finish_screen = stimuli.TextScreen(
    "Blind Spot Test",
    "Thank you for participating!\n\n"
    "Press any key to exit."
)

if key == K_2:  # No
    finish_screen.present()
else:
    second_side = "right" if first_side == "left" else "left"
    run_trial(second_side)
    finish_screen.present()


exp.keyboard.wait()

 
control.end()

