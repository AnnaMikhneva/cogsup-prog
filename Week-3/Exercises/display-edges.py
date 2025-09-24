
from expyriment import design, control, stimuli


exp = design.Experiment()
control.initialize(exp)


width, height = exp.screen.size


square_size = int(width * 0.05)


red_square = stimuli.Rectangle(size=(square_size, square_size), 
                              colour=(255, 0, 0), 
                              line_width=1,
                              position=(-width//2 + square_size//2, height//2 - square_size//2))

red_square2 = stimuli.Rectangle(size=(square_size, square_size), 
                               colour=(255, 0, 0), 
                               line_width=1,
                               position=(width//2 - square_size//2, height//2 - square_size//2))

red_square3 = stimuli.Rectangle(size=(square_size, square_size), 
                               colour=(255, 0, 0), 
                               line_width=1,
                               position=(-width//2 + square_size//2, -height//2 + square_size//2))

red_square4 = stimuli.Rectangle(size=(square_size, square_size), 
                               colour=(255, 0, 0), 
                               line_width=1,
                               position=(width//2 - square_size//2, -height//2 + square_size//2))


control.start(subject_id=1)


red_square.present(clear=True, update=False)
red_square2.present(clear=False, update=False)
red_square3.present(clear=False, update=False)
red_square4.present(clear=False, update=True)

exp.keyboard.wait()

control.end()