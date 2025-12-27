
from tkinter import *
import settings
import util
from cell import Cell

root = Tk()
root.title("Minesweeper")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.resizable(False, False)
root.configure(bg="black")

# Top frame
top_frame = Frame(
    root,
    bg="black",
    width=settings.WIDTH,
    height=util.height_perct(25)
)
top_frame.place(x=0, y=0)

Label(
    top_frame,
    text="Minesweeper",
    bg="black",
    fg="white",
    font=("", 36)
).place(x=util.width_perct(25), y=20)

# Left frame
left_frame = Frame(
    root,
    bg="black",
    width=util.width_perct(25),
    height=util.height_perct(75)
)
left_frame.place(x=0, y=util.height_perct(25))

# Center frame
center_frame = Frame(
    root,
    bg="black",
    width=util.width_perct(75),
    height=util.height_perct(75)
)
center_frame.place(
    x=util.width_perct(25),
    y=util.height_perct(25)
)

# Create grid
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        cell = Cell(x, y)
        cell.create_btn_object(center_frame)
        cell.cell_btn_object.grid(row=x, column=y)

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label.place(x=0, y=0)

Cell.randomize_mines()

root.mainloop()
