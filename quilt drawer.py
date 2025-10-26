"""
COMP0015 Quilt
"""
#Description: quilt drawer of simple graphs with input dimensions using ezgraphics.

from ezgraphics import GraphicsWindow

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 300 

N = 10   # controls the number of rows and columns in the quilt 
         # must be even to make nice looking patterns
         # must be greater than or equal to 2
    

def draw_stripes(canvas, x, y, width, height, num_lines):
    canvas.setOutline("red")
    canvas.drawRectangle(x, y, width, height)
    canvas.setOutline("black")
    increment = height / num_lines
    
    for i in range(0, num_lines + 1):
        canvas.drawLine(x, y+ (i * increment), x + width, y + (i * increment))
    
    """
    Draw stripes on the canvas at x, y, with width, height.
    num_lines is the number of stripes.
    """
    pass

def draw_chevrons(canvas, x, y, width, height, num_chevrons):
    canvas.setOutline("red")
    canvas.drawRectangle(x, y, width, height)
    canvas.setOutline("black")
    increment_height= height / num_chevrons
    increment_width= width / num_chevrons
    for i in range(0, num_chevrons//2):
        canvas.drawLine(x , y + (i * increment_height), \
                        x + width / 2 - (i * increment_width), y + height/2)
        canvas.drawLine(x , y + height - (i * increment_height),\
                        x + width / 2 - (i * increment_width), y + height/2)
        canvas.drawLine(x + width, y + (i * increment_height),\
                        x + width / 2 + (i * increment_width), y + height/2)
        canvas.drawLine(x + width, y + height - (i * increment_height),\
                        x + width / 2 + (i * increment_width), y + height/2)
    """
    Draw chevrons on the canvas at x, y, with width, height.
    """
    pass

def draw_fan(canvas, x, y, width, height, num_lines):
    canvas.setOutline("red")
    canvas.drawRectangle(x, y, width, height)
    canvas.setOutline("black")
    increment = width / num_lines
    
    for i in range(0, num_lines + 1):
        canvas.drawLine(x + width/2, y + height, x + (i * increment), y)
    """
    Draw a fan with given number of segments on the canvas at x, y, 
    with width, height.
    """
    pass

def draw_quilt(canvas, width, height, n):
    for i in range (0,N):
        patch_width = WINDOW_WIDTH/N
        patch_height = WINDOW_HEIGHT/N
        for n in range(0,N):
            choice = (i + n) % 3
            if choice == 0:
                draw_fan(canvas, i*patch_width, n*patch_height,\
                  patch_width - 1, patch_height - 1, N)
            elif choice == 1:
                draw_chevrons(canvas, i*patch_width, n*patch_height,\
                  patch_width - 1, patch_height - 1, N)
            elif choice == 2:
                draw_stripes(canvas, i*patch_width, n*patch_height,\
                  patch_width - 1, patch_height - 1, N)
    
    """ 
    draw a quilt of dimensions width, height with n patches in each row and col
    """
    pass        


def main():

    # DO NOT EDIT THIS CODE
    # Create a graphics window (width x height pixels):
    win = GraphicsWindow(WINDOW_WIDTH, WINDOW_HEIGHT)
    # Access the canvas contained in the graphics window:
    canvas = win.canvas()

    patch_width = WINDOW_WIDTH / N
    patch_height = WINDOW_HEIGHT / N

    # You can edit the code below as described in the brief
    
    #draw_stripes(canvas, 0, 0, patch_width, patch_height, 6)
    #draw_stripes(canvas, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,\
    #                patch_width - 1, patch_height - 1, 6)

    #draw_fan(canvas, 0, 0, patch_width, patch_height, 6)
    #draw_fan(canvas, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,\
    #           patch_width - 1, patch_height - 1, 6)

    #draw_chevrons(canvas, 0, 0, patch_width, patch_height, 6)
    #draw_chevrons(canvas, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,\
    #              patch_width - 1, patch_height - 1, 6)

    draw_quilt(canvas, WINDOW_WIDTH - 1, WINDOW_HEIGHT - 1, N)


    # DO NOT EDIT THIS CODE
    # Wait for the user to close the window 
    win.wait()

if __name__ == "__main__":
    main()
