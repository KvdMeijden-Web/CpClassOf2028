import tkinter as tk
def add():
    total = float(firstNumber.get()) + float(secondNumber.get())
    Result =result.config(text=total)

# Create TK window
root = tk.Tk()
root.title("Calculator")
# Add widgets in the screen
# - Header label
header = tk.Label(root, text="Calculator",font=("ariel",23))
header.pack()
# - Entry1 entry
firstNumber = tk.Entry(root,font=("ariel",23))
firstNumber.insert(0,0)
firstNumber.pack()
# - Entry2 entry
secondNumber = tk.Entry(root,font=("ariel",23))
secondNumber.pack()
# - Result label
result = tk.Label(root, text="-",font=("ariel",23))
result.pack()
# - Button: activate the "add function" button
button_calculate = tk.Button(root, text="Add", font=("ariel",23),command=add)
button_calculate.pack()
# Loop the program
root.mainloop()