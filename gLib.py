canvas=[]

def create_canvas(xsize,ysize):
    for x in range(xsize):
        canvas.append([])
        for y in range(ysize):
            canvas[x].append('   ')        

def draw_box(xsize,ysize,xpos,ypos):
    canvas[ypos][xpos]=" ┌─"
    canvas[ypos][xpos+1+xsize]="─┐ "
    canvas[ypos+1+ysize][xpos+1+xsize]="─┘ "
    canvas[ypos+1+ysize][xpos]=" └─"

    for i in range(ysize):
        canvas[ypos+i+1][xpos]=" │ "
    for i in range(xsize):
        canvas[ypos][xpos+1+i]="───"
    for i in range(ysize):
        canvas[ypos+i+1][xpos+xsize+1]=" │ "
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

def draw_map(segmentsinput):
    #segments = [" 0 "," 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8 "," 9 "," 10"," 11"]
    segments=["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   "]
    for key, value in segmentsinput.items():
        value2 = "   "
        if len(str(value)) == 1:
            value2 = " "+str(value)+" "
        elif len(str(value)) == 2:
            value2 = " "+str(value)
        else:
            value2 = str(value)
        
        if value < 20:
            value2 = "\033[1;32m"+value2+"\033[0m"
        if value > 50:
            value2 = "\033[1;31m"+value2+"\033[0m"
        else:
            value2 = "\033[1;33m"+value2+"\033[0m"




        if key == 'H11':
            segments[11] = value2
        if key == 'H10':
            segments[10] = value2
        if key == 'H9':
            segments[9] = value2
        if key == 'H8':
            segments[8] = value2
        if key == 'H7':
            segments[7] = value2
        if key == 'H6':
            segments[6] = value2
        if key == 'H5':
            segments[5] = value2
        if key == 'H4':
            segments[4] = value2
        if key == 'H3':
            segments[3] = value2
        if key == 'H2':
            segments[2] = value2
        if key == 'H1':
            segments[1] = value2
        if key == 'H0':
            segments[0] = value2

    print("                  ┌─────┬─────┐              ")
    print("                  │     │     │   ┌───┬────┐")
    print("                  │     │     │   │   │    │")
    print("                  ├─────┼───┬─┤   ├───┤    │")
    print("                  │     ├───┴─┤   │   │    │")
    print("      ┌───────┐   │     │     │   │   │    │")
    print("      │       │"+segments[10]+"├─────┤     │"+segments[11]+"├───┤    │")
    print("      │       │   │     │     │   ├─┬─┴────┤")
    print("      └─┬─────┤   │     │     │   │ │      │")
    print("        │     │   └─────┴─────┘   └─┴──────┘")
    print("        │     │"+segments[7]+"     "+segments[8]+"     "+segments[9]+" ")
    print("        ├─────┤   ┌───┬───────┐   ┌──────┐")
    print("        │     │   │   │       │   │      │")
    print("        │     │   ├───┼────┬──┤   │      │")
    print("        ├─────┤"+segments[5]+"│   │    │  │"+segments[6]+"├──────┤")
    print("        │     │   ├───┘    └──┤   │      │")
    print("        │     │   │           │   │      │")
    print("        ├─────┤   │           │   ├──────┤")
    print("        │     │   ├───┬───┬───┤   │      │")
    print("        │     │   │   │   │   │   │      │")
    print("        ├─────┤"+segments[3]+"├───┴───┴┬──┤"+segments[4]+"├──────┤")
    print("        │     │   │        │  │   │      │")
    print("        │     │   │        │  │   │      │")
    print("        └─────┘   └────────┴──┘   └──────┘ ")
    print("                      "+segments[2]+"                    ┌───┐")
    print("  ┌─────────────────┐     ┌──────────────────┤   │")
    print("  │                 │     │                  │   │")
    print("  │                 │     │                  │   │")
    print("  │                 │ "+segments[1]+" │                  │   │")
    print("  │                 │     │                  │   │")
    print("  │                 │     ├─────────────┬────┤   │")
    print("  │                 │     │             │ "+segments[0]+"└───┘")
    print("  │                 │     │             │ ┌─────┐")
    print("  └─────────────────┘     └─────────────┘ │     │")
    print("                                          │     │")
    print("                          ┌─────────────┐ └─────┘")
    print("                          │             │")
    print("                          │             │")
    print("                          └─────────────┘")
