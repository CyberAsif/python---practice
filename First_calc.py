import tkinter as tk

root = tk.Tk()
root.title("Phone Calculator")
root.geometry("330x520")
root.config(bg="#1C1C1C")
root.resizable(False, False)

# ---------------- Display ----------------
display = tk.Entry(root, font=("Helvetica", 28), bg="#1C1C1C", fg="white",
                   border=0, justify="right", insertbackground="white")
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=25, padx=10, pady=(20, 10), sticky="nsew")

# ---------------- Functions ----------------
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = display.get().replace("×", "*").replace("÷", "/")
            result = eval(expression)
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif text == "C":
        display.delete(0, tk.END)
    elif text == "⌫":
        display.delete(len(display.get())-1)
    else:
        display.insert(tk.END, text)

# ---------------- Colors ----------------
colors = {
    "nums": "#333333",
    "ops": "#FF9500",
    "func": "#A5A5A5"
}

# ---------------- Buttons ----------------
buttons = [
    ["C", "⌫", "÷", "×"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", ""]
]

# ---------------- Grid Layout ----------------
for i in range(5):
    root.rowconfigure(i+1, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

for i, row in enumerate(buttons):
    for j, b in enumerate(row):
        if b == "":
            continue
        if b in ["÷", "×", "-", "+", "="]:
            color = colors["ops"]
        elif b in ["C", "⌫"]:
            color = colors["func"]
        else:
            color = colors["nums"]
        btn = tk.Button(root, text=b, bg=color, fg="white",
                        font=("Helvetica", 22, "bold"), bd=0, relief="flat")
        btn.grid(row=i+1, column=j, sticky="nsew", padx=4, pady=4)
        btn.bind("<Button-1>", click)

# Widen the 0 button
root.grid_columnconfigure(0, weight=2)

root.mainloop()