import tkinter as tk

def print_selection():
    slan = lng.get()
    print(f"Selected Programming Language: {slan}")


root = tk.Tk()
root.title("Programming Language Selector")


lng = tk.StringVar(root)
lng.set("Python")  


lngs = ["Python", "Java", "C++"]
menu = tk.OptionMenu(root, lng, *lngs)
menu.pack(pady=10)


btn = tk.Button(root, text="Select Language", command=print_selection)
btn.pack(pady=10)


root.mainloop()
