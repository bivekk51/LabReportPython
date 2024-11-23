import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")
        
        # Entry box to display the result
        self.result_var = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.result_var, font=("Arial", 24), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons for digits and operations
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '=', '+'
        ]
        
        row_val = 1
        col_val = 0
        
        for button in buttons:
            tk.Button(master, text=button, width=5, height=2, command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:  # Reset column after 4 buttons
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                # Evaluate the expression and update the entry
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            # Update the entry with the clicked button
            self.result_var.set(self.result_var.get() + char)

# Create the main window
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
