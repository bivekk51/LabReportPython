import tkinter as tk

def on_button_click():
    print("Button Clicked")

# Create the main window
root = tk.Tk()
root.title("Welcome Window")

# Create a label
welcome_label = tk.Label(root, text="Welcome to GUI Programming")
welcome_label.pack(pady=20)

# Create a button
click_me_button = tk.Button(root, text="Click Me!", command=on_button_click)
click_me_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
