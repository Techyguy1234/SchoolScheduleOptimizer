canvas=[]

def create_canvas(xsize,ysize):
    for x in range(xsize):
        canvas.append([])
        for y in range(ysize):
            canvas[x].append('   ')        

def draw_box(xsize,ysize,xpos,ypos):
    canvas[ypos][xpos]=" ┌─"
    canvas[ypos][xpos+1+xsize]="┐  "
    canvas[ypos+1+ysize][xpos+1+xsize]="┘  "
    canvas[ypos+1+ysize][xpos]=" └─"

    for i in range(ysize):
        canvas[ypos+i+1][xpos]=" │ "
    for i in range(xsize):
        canvas[ypos][xpos+1+i]="───"
    for i in range(ysize):
        canvas[ypos+i+1][xpos+xsize+1]="│  "
    for i in range(xsize):
        canvas[ypos+ysize+1][xpos+1+i]="───"

def print_canvas():
    for y in canvas:
        a=""
        for x in y:
            a=a+str(x)
        print(a)

create_canvas(15,15)
draw_box(3,5,2,2)
draw_box(3,2,4,3)
draw_box(5,1,7,8)

print_canvas()