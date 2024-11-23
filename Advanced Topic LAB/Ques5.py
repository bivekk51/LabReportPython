import tkinter as tk

def print_selection():
    slan = lng.get()
    print(f"Selected Programming Language: {slan}")

# Create the main window
root = tk.Tk()
root.title("Programming Language Selector")

# Variable to store the selected language
lng = tk.StringVar(root)
lng.set("Python")  # Set the default option

# Dropdown menu (OptionMenu) for selecting programming lngs
lngs = ["Python", "Java", "C++"]
menu = tk.OptionMenu(root, lng, *lngs)
menu.pack(pady=10)

# Button to print the selected option
btn = tk.Button(root, text="Select Language", command=print_selection)
btn.pack(pady=10)

# Run the application
root.mainloop()
