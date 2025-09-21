from expyriment import design, control, stimuli
from expyriment.misc import geometry
import math

def create_labeled_polygon(n_sides, side_length, color, position, label, reference_height=None):
    """
    Parameters:
    n_sides: Number of sides for the polygon
    side_length: Length of each side
    color: Color of the polygon (RGB tuple)
    position: Position of the polygon (x, y)
    label: Text label for the polygon
    reference_height: If provided, scale the polygon to match this height
    
    Returns:
    A tuple containing (polygon, line, label) stimuli objects
    """

    if n_sides == 3:  
        height = math.sqrt(3) / 2 * side_length
    elif n_sides == 4:  
        height = side_length
    elif n_sides == 6: 
        height = 2 * side_length
    else:  
        height = side_length / math.tan(math.pi / n_sides) * 2
    
    if reference_height is not None:
        scale_factor = reference_height / height
        side_length *= scale_factor
        height = reference_height
    
    vertices = geometry.vertices_regular_polygon(n_sides, side_length)
    polygon = stimuli.Shape(
        colour=color,
        position=position,
        vertex_list=vertices
    )
    
    line = stimuli.Line(
        line_width=3,
        colour=(255, 255, 255), 
        start_point=(position[0], position[1] + height/2), 
        end_point=(position[0], position[1] + height/2 + 50)  
    )
    

    text_label = stimuli.TextLine(
        text=label,
        text_colour=(255, 255, 255),  
        position=(position[0], position[1] + height/2 + 50 + 20)  
    )
    
    return polygon, line, text_label, height


exp = design.Experiment(name="Labeled Shapes with Function")


control.initialize(exp)


triangle, triangle_line, triangle_label, triangle_height = create_labeled_polygon(
    n_sides=3,
    side_length=50,
    color=(128, 0, 128), 
    position=(-100, 0),   
    label="triangle"
)


hexagon, hexagon_line, hexagon_label, _ = create_labeled_polygon(
    n_sides=6,
    side_length=25,  
    color=(255, 255, 0), 
    position=(100, 0),    
    label="hexagon",
    reference_height=triangle_height  
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