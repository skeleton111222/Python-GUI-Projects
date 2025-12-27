# from tkinter import Button,Label
# import random
# import settings
# import ctypes
# import sys

# class Cell:
#     all=[]
#     cell_count= settings.CELL_COUNT
#     cell_count_label=None
#     def __init__(self, x, y, is_mine=False):
#         self.is_mine = is_mine
#         self.cell_btn_object = None
#         self.is_opened = False
#         self.is_mine_candidate= False
#         self.x=x
#         self.y=y

#         Cell.all.append(self)

#     def create_btn_object(self, location):
#         # btn= Button(location, text=f"{self.x}{self.y}", width=12, height=4)
#         btn= Button(location, width=12, height=4)

#         btn.bind('<Button-1>', self.left_click)

#         btn.bind('<Button-3>', self.right_click)

#         self.cell_btn_object= btn

#     @staticmethod
#     def create_cell_count_label(location):
#         label= Label(location, bg="black", fg="white", text=f"Cells left: {Cell.cell_count}", font=("",30))
#         Cell.cell_count_label= label

#     def left_click(self, event):
#         # print(event)
#         # print("I am left")
#         if self.is_mine:
#             self.show_mine()
        
#         else:
#             if self.surrounded_cells_mines_length == 0:
#                 for cell_obj in self.surrounded_cells:
#                     cell_obj.show_cell()
#             self.show_cell()
#             #if mine count == cels left count, player won
#             if Cell.cell_count == settings.MINES_COUNT:
#                 ctypes.windll.user32.MessageBoxW(0, "Congratulations! You Won the Game","Game Over", 0)
#         #cancel left and right click events if cell is already opened:
#         self.cell_btn_object.unbind("<button-1>")
#         self.cell_btn_object.unbind("<Button-3>")

#     def get_cell_by_axis(self, x, y):
#         for cell in Cell.all:
#             if cell.x == x and cell.y == y:
#                 return cell

#     @property
#     def surrounded_cells(self):
#         cells= [
#             self.get_cell_by_axis(self.x-1, self.y-1),
#             self.get_cell_by_axis(self.x-1, self.y),
#             self.get_cell_by_axis(self.x-1, self.y+1),
#             self.get_cell_by_axis(self.x, self.y-1),
#             self.get_cell_by_axis(self.x+1, self.y-1),
#             self.get_cell_by_axis(self.x+1, self.y),
#             self.get_cell_by_axis(self.x+1, self.y+1),
#             self.get_cell_by_axis(self.x, self.y+1),
#         ]
#         # print(cells)
#         cells= [cell for cell in cells if cell is not None]
#         return cells

#     @property
#     def surrounded_cells_mines_length(self):
#         counter= 0
#         for Cell in self.surrounded_cells:
#             if cell.is_mine:
#                 counter+=1

#         return counter

#     def show_cell(self):
#         if not self.is_opened:
#             Cell.cell_count-=1
#             self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
#             # print(self.surrounded_cells_mines_length)
#             # Replace text of cell count label with the newer count
#             if Cell.cell_count_label:
#                 Cell.cell_count_label.configure(text=f"Cells left: {Cell.cell_count}")
#             #if this was the mine candidate then for safety we should configure the bg color to system one
#             self.cell_btn_object.configure(bg="SystemButtonFace")
#         #Mark the cell as opened(use it as the last line of this method)
#         self.is_opened= True

    
#     def show_mine(self):
#         self.cell_btn_object.configure(bg="red")
#         ctypes.windll.user32.MessageBoxW(0, "You clicked a Mine","Game Over", 0)
#         sys.exit()

#     def right_click(self, event):
#         if not self.is_mine_candidate:
#             self.cell_btn_object.configure(bg="orange")

#         else:
#             self.cell_btn_object.configure(bg="SystemButtonFace")
#             self.is_mine_candidate=False

#         # print(event)
#         # print("I am right")

#     @staticmethod
#     def randomize_mines():
#         picked_cells= random.sample(
#             Cell.all, settings.MINES_COUNT
#         )
#         for picked_cells in picked_cells:
#             picked_cells.is_mine= True

#     def __repr__(self):
#         return f"Cell({self.x}, {self.y})"



from tkinter import Button, Label, messagebox
import random
import settings
import sys

class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_mine = False
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(location, width=10, height=3)
        btn.bind("<Button-1>", self.left_click)
        btn.bind("<Button-3>", self.right_click)
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        label = Label(
            location,
            bg="black",
            fg="white",
            text=f"Cells left: {Cell.cell_count}",
            font=("", 24)
        )
        Cell.cell_count_label = label

    def left_click(self, event):
        if self.is_opened or self.is_mine_candidate:
            return

        if self.is_mine:
            self.show_mine()
            return

        self.show_cell()

        if self.surrounded_cells_mines_length == 0:
            for cell in self.surrounded_cells:
                cell.left_click(None)

        if Cell.cell_count == settings.MINES_COUNT:
            messagebox.showinfo("Game Over", "🎉 Congratulations! You Won!")

    def right_click(self, event):
        if self.is_opened:
            return

        if not self.is_mine_candidate:
            self.cell_btn_object.configure(text="🚩", fg="red")
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(text="", fg="black")
            self.is_mine_candidate = False

    def show_cell(self):
        if self.is_opened:
            return

        Cell.cell_count -= 1
        number = self.surrounded_cells_mines_length

        colors = {
            0: "black",
            1: "blue",
            2: "green",
            3: "red",
            4: "purple",
            5: "maroon",
            6: "cyan",
            7: "black",
            8: "gray"
        }

        self.cell_btn_object.configure(
            text=number if number > 0 else "",
            state="disabled",
            disabledforeground=colors[number]
        )

        if Cell.cell_count_label:
            Cell.cell_count_label.configure(
                text=f"Cells left: {Cell.cell_count}"
            )

        self.is_opened = True

    def show_mine(self):
        self.cell_btn_object.configure(bg="red")
        messagebox.showinfo("Game Over", "💥 You clicked a mine!")
        sys.exit()

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x-1, self.y-1),
            self.get_cell_by_axis(self.x-1, self.y),
            self.get_cell_by_axis(self.x-1, self.y+1),
            self.get_cell_by_axis(self.x, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y),
            self.get_cell_by_axis(self.x+1, self.y+1),
            self.get_cell_by_axis(self.x, self.y+1),
        ]
        return [cell for cell in cells if cell]

    @property
    def surrounded_cells_mines_length(self):
        return sum(cell.is_mine for cell in self.surrounded_cells)

    @staticmethod
    def randomize_mines():
        mines = random.sample(Cell.all, settings.MINES_COUNT)
        for cell in mines:
            cell.is_mine = True
