from expyriment import design, control, stimuli

def create_hermann_grid(square_size, spacing, rows, columns, 
                       square_color, background_color):
    
    exp = design.Experiment()
    control.initialize(exp)
    

    width, height = exp.screen.size
    

    grid_width = columns * square_size + (columns - 1) * spacing
    grid_height = rows * square_size + (rows - 1) * spacing

    start_x = -grid_width // 2 + square_size // 2
    start_y = grid_height // 2 - square_size // 2
    

    squares = []
    for i in range(rows):
        for j in range(columns):
            x_pos = start_x + j * (square_size + spacing)
            y_pos = start_y - i * (square_size + spacing)
            
            square = stimuli.Rectangle(size=(square_size, square_size),
                                      colour=square_color,
                                      position=(x_pos, y_pos))
            squares.append(square)
    
    control.start()
    

    background = stimuli.Rectangle(size=(width, height),
                                  colour=background_color,
                                  position=(0, 0))
    

    background.present(clear=True, update=False)

    for idx, square in enumerate(squares):
        if idx == len(squares) - 1:
            square.present(clear=False, update=True) 
        else:
            square.present(clear=False, update=False)
    
    
    exp.keyboard.wait()
    
    control.end()


create_hermann_grid(square_size=70, spacing=15, rows=8, columns=8,
                       square_color=(0, 0, 0), background_color=(255, 255, 255))

#  spacing is crucial - too close or too far weakens the illusion
#  color contrast affects illusion strength (black-white is the best)
#  more than 4 rows and columns because the more intersections - the stronger illusion