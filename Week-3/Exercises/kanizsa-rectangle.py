from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY

def display_kanizsa_rectangle(aspect_ratio, rectangle_scale, circle_scale):

    
    exp = design.Experiment()
    control.initialize(exp)
    
    width, height = exp.screen.size
    

    rect_width = int(width * rectangle_scale)
    rect_height = int(rect_width / aspect_ratio)

    circle_diameter = int(rect_width * circle_scale)
    
    kanizsa_rectangle = stimuli.Rectangle(size=(rect_width, rect_height),
                                         colour=C_GREY,
                                         position=(0, 0))
    
    center_x, center_y = 0, 0
    

    circle_positions = [
        (center_x - rect_width//2, center_y + rect_height//2),  
        (center_x + rect_width//2, center_y + rect_height//2), 
        (center_x - rect_width//2, center_y - rect_height//2),  
        (center_x + rect_width//2, center_y - rect_height//2)  
    ]
    
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
    kanizsa_rectangle.present(clear=False, update=True)
    
    exp.keyboard.wait()
    
    control.end()
    
display_kanizsa_rectangle(aspect_ratio=1.5, rectangle_scale=0.25, circle_scale=0.2) # the best
# display_kanizsa_rectangle(aspect_ratio=3.5, rectangle_scale=0.15, circle_scale=0.3)
# display_kanizsa_rectangle(aspect_ratio=3.5, rectangle_scale=0.35, circle_scale=0.45)

# 0.30-0.35 rectangle scale: Circles farther apart - illusion may weaken
# 0.40-0.45 circle scale: Overlapping may disrupt illusion
# Otherwise it is kinda fine for me.