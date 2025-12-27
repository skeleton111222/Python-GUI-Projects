from tkinter import *
import settings
import util
from cell import Cell
#Root Frame Data
root=Tk()
root.title("Minesweeper Games")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.resizable(False,False)
root.configure(bg="black")

#Nested Frame Data
top_frame= Frame(root, bg="black", width=settings.WIDTH, height=util.height_perct(25))
top_frame.place(x=0, y=0)

game_title=Label(top_frame, bg="black", fg="white", text="Minesweeper Game", font=('',48))
game_title.place(x=util.width_perct(25), y=0)

left_frame= Frame(root, bg="black", width=util.width_perct(25), height=util.height_perct(75))
left_frame.place(x=0, y=util.height_perct(25))

center_frame = Frame(root, bg="black", width=util.width_perct(75), height=util.height_perct(75))
center_frame.place(x= util.width_perct(25), y=util.height_perct(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c= Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(row=x,column=y)

# print(len(Cell.all))
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label.place(x=0,y=0)
Cell.randomize_mines()

root.mainloop()