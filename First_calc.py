import tkinter as tk
from tkinter import font

def create_calculator():
    """
    Creates a GUI calculator using tkinter.
    Supports basic arithmetic operations and clear functionality.
    """
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("300x400")
    root.resizable(False, False)

    # Custom font
    custom_font = font.Font(size=14)

    # Entry widget for display
    display = tk.Entry(root, font=custom_font, bd=10, insertwidth=2, width=14, borderwidth=4, justify="right")
    display.grid(row=0, column=0, columnspan=4, pady=10)

    # Button layout
    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+',
        'C'
    ]

    # Button click function
    def button_click(item):
        if item == '=':
            try:
                result = eval(display.get())
                display.delete(0, tk.END)
                display.insert(tk.END, str(result))
            except:
                display.delete(0, tk.END)
                display.insert(tk.END, "Error")
        elif item == 'C':
            display.delete(0, tk.END)
        else:
            display.insert(tk.END, item)

    # Create buttons
    row = 1
    col = 0
    for button in buttons:
        if button == '=':
            tk.Button(root, text=button, padx=20, pady=20, font=custom_font, command=lambda b=button: button_click(b)).grid(row=row, column=col, columnspan=2, sticky="nsew")
        elif button == 'C':
            tk.Button(root, text=button, padx=20, pady=20, font=custom_font, command=lambda b=button: button_click(b)).grid(row=row+1, column=col, columnspan=4, sticky="nsew")
        else:
            tk.Button(root, text=button, padx=20, pady=20, font=custom_font, command=lambda b=button: button_click(b)).grid(row=row, column=col, sticky="nsew")
        col += 1
        if col > 3:
            col = 0
            row += 1

    # Configure grid weights
    for i in range(5):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()

if __name__ == "__main__":
    create_calculator()
