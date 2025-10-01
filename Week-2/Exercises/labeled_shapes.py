from expyriment import design, control, stimuli
from expyriment.misc import geometry
import math

exp = design.Experiment(name="Labeled Shapes")

control.initialize(exp)


triangle_vertices = geometry.vertices_regular_polygon(3, 50)
triangle = stimuli.Shape(
    colour=(128, 0, 128),  
    position=(-100, 0),    
    vertex_list=triangle_vertices
)

# Height of equilateral triangle: h = (√3/2) * side ≈ 43.3
triangle_height = math.sqrt(3) / 2 * 50

# For a regular hexagon, the height is 2 * side_length
# We want it to match the triangle's height, so side_length = triangle_height / 2
hexagon_side_length = triangle_height / 2
hexagon_vertices = geometry.vertices_regular_polygon(6, hexagon_side_length)
hexagon = stimuli.Shape(
    colour=(255, 255, 0),  
    position=(100, 0),    
    vertex_list=hexagon_vertices
)

# Line for the triangle (50px long, 3px wide)
triangle_line = stimuli.Line(
    line_width=3,
    colour=(255, 255, 255), 
    start_point=(-100, triangle_height/2),  
    end_point=(-100, triangle_height/2 + 50)  
)


hexagon_line = stimuli.Line(
    line_width=3,
    colour=(255, 255, 255),  
    start_point=(100, triangle_height/2),  
    end_point=(100, triangle_height/2 + 50)  
)


triangle_label = stimuli.TextLine(
    text="triangle",
    text_colour=(255, 255, 255),  
    position=(-100, triangle_height/2 + 50 + 20)  
)

hexagon_label = stimuli.TextLine(
    text="hexagon",
    text_colour=(255, 255, 255),  
    position=(100, triangle_height/2 + 50 + 20)  
)


control.start(subject_id=1)


triangle.present(clear=True, update=False)        
hexagon.present(clear=False, update=False)       
triangle_line.present(clear=False, update=False) 
hexagon_line.present(clear=False, update=False)  
triangle_label.present(clear=False, update=False) 
hexagon_label.present(clear=False, update=True)   

exp.keyboard.wait()

control.end()