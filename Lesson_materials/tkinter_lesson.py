import tkinter as tk

root = tk.Tk()
root.title("Basic Tkinter")

# Canvas
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()
 
# Label
label = tk.Label(root, text="Hello")
label.pack()
#label.place(x=50, y=50)

root.mainloop()
# def toggle_text():
#     if label.cget("text") == "Hello":
#         label.config(text="Goodbye")
#     else:
#         label.config(text="Hello")


# # Label
# label = tk.Label(root, text="Hello")
# label.pack()

# # Button
# button = tk.Button(root, text="Toggle text", command=toggle_text)
# button.pack()

