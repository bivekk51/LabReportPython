import tkinter as tk

def button1_action():
    print("Button 1 clicked!")

def button2_action():
    print("Button 2 clicked!")

def button3_action():
    print("Button 3 clicked!")

root = tk.Tk()
root.title("Vertical Button Layout")

button1 = tk.Button(root, text="Button 1", command=button1_action)
button1.pack(pady=10)  

button2 = tk.Button(root, text="Button 2", command=button2_action)
button2.pack(pady=10)

button3 = tk.Button(root, text="Button 3", command=button3_action)
button3.pack(pady=10)

root.mainloop()
