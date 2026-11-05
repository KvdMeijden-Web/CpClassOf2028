import tkinter as tk
from interface import Interface


def greet(name):
    if name == "":
        return "Please enter your name!"

    return f"Hello, {name}!"


def main():
    root = tk.Tk()
    app = Interface(root, greet)
    root.mainloop()


if __name__ == "__main__":
    main()