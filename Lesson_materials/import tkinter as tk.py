import tkinter as tk

def toggle_text():
        search = search_entry.get()
        subheader.config(text=search)

root = tk.Tk()
root.title("Pokedesk")
root.geometry("1200x900")

#header
header = tk.Label(root,text="Pokedesk")
header.config(font=('Ariel',40))
header.pack()

#subheader
subheader = tk.Label(root,text="Search your pokemon")
subheader.config(font=('Ariel',25))
subheader.pack()

#search entry
search_entry= tk.Entry(root)
search_entry.config(font =('Ariel',25))
search_entry.pack()

search_button= tk.Button(root, text="search", command=toggle_text)
search_button.config(font =('Ariel',25))
search_button.pack()

root.mainloop()