from expyriment import design, control, stimuli
from expyriment.misc import geometry
import math

# Create an experiment object
exp = design.Experiment(name="Labeled Shapes")

# Initialize the experiment
control.initialize(exp)

# Create a purple equilateral triangle (side length: 50)
# Using vertices_regular_polygon from geometry module
triangle_vertices = geometry.vertices_regular_polygon(3, 50)
triangle = stimuli.Shape(
    colour=(128, 0, 128),  # Purple color
    position=(-100, 0),    # Left shape: 100 pixels left of center
    vertex_list=triangle_vertices
)

# Create a yellow regular hexagon that matches the triangle's height
# Height of equilateral triangle: h = (√3/2) * side ≈ 43.3
triangle_height = math.sqrt(3) / 2 * 50

# For a regular hexagon, the height is 2 * side_length
# We want it to match the triangle's height, so side_length = triangle_height / 2
hexagon_side_length = triangle_height / 2
hexagon_vertices = geometry.vertices_regular_polygon(6, hexagon_side_length)
hexagon = stimuli.Shape(
    colour=(255, 255, 0),  # Yellow color
    position=(100, 0),     # Right shape: 100 pixels right of center
    vertex_list=hexagon_vertices
)

# Create white vertical lines going upwards from the top of each shape
# Line for the triangle (50px long, 3px wide)
triangle_line = stimuli.Line(
    line_width=3,
    colour=(255, 255, 255),  # White color
    start_point=(-100, triangle_height/2),  # Start at top of triangle
    end_point=(-100, triangle_height/2 + 50)  # End 50px above start point
)

# Line for the hexagon (50px long, 3px wide)
hexagon_line = stimuli.Line(
    line_width=3,
    colour=(255, 255, 255),  # White color
    start_point=(100, triangle_height/2),  # Start at top of hexagon (same height as triangle)
    end_point=(100, triangle_height/2 + 50)  # End 50px above start point
)

# Create shape labels 20px away from the upper end of the segments
triangle_label = stimuli.TextLine(
    text="triangle",
    text_colour=(255, 255, 255),  # White color
    position=(-100, triangle_height/2 + 50 + 20)  # 20px above the line end
)

hexagon_label = stimuli.TextLine(
    text="hexagon",
    text_colour=(255, 255, 255),  # White color
    position=(100, triangle_height/2 + 50 + 20)  # 20px above the line end
)

# Start running the experiment
control.start(subject_id=1)

# Present all elements
triangle.present(clear=True, update=False)        # Present triangle without clearing
hexagon.present(clear=False, update=False)        # Present hexagon without clearing
triangle_line.present(clear=False, update=False)  # Present triangle line without clearing
hexagon_line.present(clear=False, update=False)   # Present hexagon line without clearing
triangle_label.present(clear=False, update=False) # Present triangle label without clearing
hexagon_label.present(clear=False, update=True)   # Present hexagon label and update display

# Leave them on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()