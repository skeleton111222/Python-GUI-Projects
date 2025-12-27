import tkinter as tk
def display():
    name=name_entry.get()
    password=pass_entry.get()
    print(f"Your name is: {name}")
    display_label.config(text=f"Your name is: {name}")
    display_label_pass.config(text=f"Your password is: {password}")
root=tk.Tk()
root.title('Login')
root.geometry("300x300+0+0")
name= tk.Label(root, text="Name:")
name.grid(row=0, column=0)

name_entry=tk.Entry(root)
name_entry.grid(row=0,column=2)

password= tk.Label(root, text="Password:")
password.grid(row=1, column=0)

pass_entry=tk.Entry(root)
pass_entry.grid(row=1,column=2)

button=tk.Button(root, text="press", command= display)
button.grid(row=2, column=0)

display_label=tk.Label(root, text="")
display_label.grid(row=3, column=0)

display_label_pass=tk.Label(root, text="")
display_label_pass.grid(row=4, column=0)
root.mainloop()