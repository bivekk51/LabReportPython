import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    
    if not name or not age or not gender:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
    else:
        print(f"Name: {name}, Age: {age}, Gender: {gender}")

# Create the main window
root = tk.Tk()
root.title("User Information Form")

# Create and place the Name label and entry
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Create and place the Age label and entry
tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

# Create and place the Gender label and radiobuttons
tk.Label(root, text="Gender:").grid(row=2, column=0, padx=10, pady=5)
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, sticky='w')
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=1, sticky='e')

# Create and place the Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
