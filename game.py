from tkinter import *
import time
import random
game_height = 700
game_width = game_height
rectangles = 40 #số ô vuông trên mỗi hàng
space_size = (game_height)/rectangles
background = 'green'#màu background
limit_rectangle = 800 #số vật cản
color_arg = 'red' #color nhân vật
color_wall = 'blue'# màu tường
step = space_size #bước đi
# bấm n để tạo game mới
window = Tk()

class wall:
    def __init__(self):
        self.limit = limit_rectangle
        self.squares = []
        for i in range(self.limit):
            x = random.randint(0,rectangles-1)*space_size
            y = random.randint(0,rectangles-1)*space_size
            if x==space_size and y==space_size or x==(rectangles-1)*space_size and y==(rectangles-1)*space_size or x==(rectangles-1)*space_size-1 and y==(rectangles-1)*space_size-1:
                continue
            square = canvas.create_rectangle(x,y,x+space_size,y+space_size,fill=color_wall)
            self.squares.append(square)
            self.squares.insert(0,[x,y])
def check_wall(Wall,coordinate,direction):
    for i in range(0,Wall.limit):
        if Wall.squares[i] == [coordinate[0]+step,coordinate[1]] and direction=='right':
            return True
        if Wall.squares[i] == [coordinate[0],coordinate[1]-step] and direction=='up':
            return True
        if Wall.squares[i] == [coordinate[0],coordinate[1]+step] and direction=='down':
            return True
        if Wall.squares[i] == [coordinate[0]-step,coordinate[1]] and direction=='left':
            return True
    return False
def move(direction,Wall):
    coordinates = canvas.coords(arg)
    if check_win(coordinates):
        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,text='you win!',font=('Comic',50))
    if direction=='left' and (coordinates[0]>0):
        if check_wall(Wall,coordinates,direction)is False :
            canvas.move(arg,-step,0)
    elif direction=='right' and coordinates[2]<game_width:
        if check_wall(Wall,coordinates,direction)is False :
            canvas.move(arg,step,0)
    elif direction=='up' and coordinates[1]>0:
        if check_wall(Wall,coordinates,direction)is False :
            canvas.move(arg,0,-step)
    elif direction=='down' and coordinates[3]<game_height:
        if check_wall(Wall,coordinates,direction)is False :
            canvas.move(arg,0,step)  
def newgame():
    global arg,Wall,final
    canvas.delete(ALL)
    arg = canvas.create_rectangle(space_size,space_size,2*space_size,2*space_size,fill=color_arg)
    final = canvas.create_rectangle((rectangles-1)*space_size,
(rectangles-1)*space_size,
(rectangles-1)*space_size+space_size,
(rectangles-1)*space_size+space_size,
fill='yellow')
    del Wall.squares
    Wall = wall()  
    print(Wall.squares)
def check_win(coordinates):
    if coordinates[0] == (rectangles-1)*space_size and coordinates[1] == (rectangles-1)*space_size:
        return True
    False
window.title('game hay')
canvas = Canvas(window,bg=background,height=game_height,width=game_width)
canvas.pack()

window.resizable(False,False)
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2)-(window_width/2))
y = int((screen_height/2)-(window_height/2))
#window.geometry(f"{window_width}x{window_height}+{x}+{y}")
Button(window,text='quit',command=quit,bg='purple',font=('Comic',15)).pack(side='bottom')
arg = canvas.create_rectangle(space_size,space_size,2*space_size,2*space_size,fill=color_arg)
final = canvas.create_rectangle((rectangles-1)*space_size,(rectangles-1)*space_size,
(rectangles-1)*space_size+space_size,
(rectangles-1)*space_size+space_size,fill='yellow')
Wall = wall()
window.bind('<n>',lambda even: newgame())
window.bind('<Up>',lambda even: move('up',Wall))
window.bind('<Down>',lambda even: move('down',Wall))
window.bind('<Left>',lambda even: move('left',Wall))
window.bind('<Right>',lambda even: move('right',Wall))
print(Wall.squares)
'''time.sleep(1)
canvas.move(arg,step,0)'''
window.mainloop()