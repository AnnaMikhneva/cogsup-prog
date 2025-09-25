from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY


exp = design.Experiment()
control.initialize(exp)


width, height = exp.screen.size


square_size = int(width * 0.25)  
circle_diameter = int(square_size * 0.3)  
kanizsa_square = stimuli.Rectangle(size=(square_size, square_size),
                                  colour=C_GREY,
                                  position=(0, 0))

center_x, center_y = 0, 0  


circle_positions = [
    (center_x - square_size//2, center_y + square_size//2),  
    (center_x + square_size//2, center_y + square_size//2),  
    (center_x - square_size//2, center_y - square_size//2),  
    (center_x + square_size//2, center_y - square_size//2)]


circles = []
colours = [(0, 0, 0), (0, 0, 0), (255, 255, 255), (255, 255, 255)]  

for i, position in enumerate(circle_positions):
    circle = stimuli.Circle(radius=circle_diameter//2, 
                           colour=colours[i],
                           position=position)
    circles.append(circle)


control.start()


background = stimuli.Rectangle(size=(width, height), 
                              colour=C_GREY,
                              position=(0, 0))


background.present(clear=True, update=False)
circles[0].present(clear=False, update=False)
circles[1].present(clear=False, update=False)
circles[2].present(clear=False, update=False)
circles[3].present(clear=False, update=False)
kanizsa_square.present(clear=False, update=True)


exp.keyboard.wait()


control.end()

