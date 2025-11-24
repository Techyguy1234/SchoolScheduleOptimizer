def visualize():
    draw_box(3,1)

def draw_box(xsize,ysize):
    a=""
    for i in range(xsize):
        a=a+"───"
    print("┌"+a+"┐")
    for i in range(ysize):
        print("│"+a.replace('─',' ')+"│")
    print("└"+a+"┘")
