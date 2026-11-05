import tkinter as tk

class Interface:
    def __init__(self, root, greet_function):
        self.root = root
        self.greet_function = greet_function

        self.root.title("My First GUI")
        self.root.geometry("400x300")

        self.title = tk.Label(
            self.root,
            text="Welcome!",
            font=("Arial", 20)
        )
        self.title.pack(pady=20)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=10)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)

        self.greet_button = tk.Button(
            self.root,
            text="Say Hello",
            command=self.on_button_click
        )
        self.greet_button.pack(pady=10)

    def on_button_click(self):
        name = self.name_entry.get()
        result = self.greet_function(name)
        self.result_label.config(text=result)