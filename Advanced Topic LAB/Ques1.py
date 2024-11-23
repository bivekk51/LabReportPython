import tkinter as tk

def on_button_click():
    print("Button Clicked")


root = tk.Tk()
root.title("Welcome Window")


welcome_label = tk.Label(root, text="Welcome to GUI Programming")
welcome_label.pack(pady=20)

click_me_button = tk.Button(root, text="Click Me!", command=on_button_click)
click_me_button.pack(pady=10)


root.mainloop()
