import tkinter as tk

def toggle_text():
    if label.cget("text") == "Hello":
        label.config(text="Goodbye")
    else:
        label.config(text="Hello")

root = tk.Tk()
root.title("Hello Goodbye")

# Canvas
canvas = tk.Canvas(root, width=900, height=600, bg="pink")
canvas.pack()

# # Label
label = tk.Label(canvas, text="Hello")

label.config(anchor='center',
             font=('Ariel',32),
             bg="pink")
label.place(x=400, y=20)
#button
button = tk.Button(canvas,text="clickme!",command=toggle_text)
button.config(anchor='center',
             font=('Ariel',32),
             bg="pink")
button.place(x=350, y=100)

root.mainloop()




# # Label
# label = tk.Label(root, text="Hello")
# label.pack()

# # Button
# button = tk.Button(root, text="Toggle text", command=toggle_text)
# button.pack()

