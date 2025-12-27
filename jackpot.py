import tkinter as tk

import random
global jackpot_number
jackpot_number =random.randint(1,100)
global counter

counter =1

def jackpot ():

    global counter

    user_input= guess_int.get()
    if(user_input!=jackpot_number):
        if(user_input>jackpot_number):
            print("Hint: Enter smaller number.")
            display_result.insert(tk.END,"Hint : Enter smaller number.")
        else: 
            print ( "Hint: Enter larger number.")
            display_result.insert(tk.END,"Hint : Enter larger number.")
        counter+=1

    else: 
        print (f"congratulations you have won jackpot in {counter} attempts.")
        display_result.insert(tk.END,f"congratulations you have won jackpot in {counter} attempts.")

    clear_entries()

def clear_entries():
    guess_input.delete (0,tk.END)
root=tk.Tk()
root.title('Jackpot')
gui_label=tk.Label(root, text='Win Jackpot')
gui_label.grid(row=0, columnspan =3, padx=10, pady=10)
guess_label=tk.Label(root,text="Enter your guess")
guess_label.grid(row=1, column=0 ,padx=10, pady=10)
guess_int =tk.IntVar()
guess_input =tk.Entry(root, textvariable=guess_int)
guess_input.grid(row=1, column=1 ,padx=10, pady=10)
submit_btn=tk.Button(root, text='Try Jackpot',command=jackpot)
submit_btn.grid(row=1, column=2 ,padx=10, pady=10)
display_result=tk.Listbox(root, width=50)
display_result.grid(row=2, columnspan=3 ,padx=10, pady=10)
root.mainloop()