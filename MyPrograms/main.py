import tkinter as tk

# -----------------------------
# Apple Style Calculator (Python)
# -----------------------------

root = tk.Tk()
root.title("Apple Calculator")
root.geometry("360x560")
root.resizable(False, False)
root.configure(bg="#000000")

expression = ""

# -----------------------------
# Display
# -----------------------------
display_var = tk.StringVar()
display_var.set("0")

display = tk.Label(
    root,
    textvariable=display_var,
    font=("Helvetica", 42),
    bg="#000000",
    fg="white",
    anchor="e",
    padx=20
)
display.pack(fill="both", pady=(30, 20))

# -----------------------------
# Functions
# -----------------------------
def press(value):
    global expression

    if value == "=":
        try:
            result = str(eval(expression))
            display_var.set(result)
            expression = result
        except:
            display_var.set("Error")
            expression = ""

    elif value == "C":
        expression = ""
        display_var.set("0")

    elif value == "⌫":
        expression = expression[:-1]
        display_var.set(expression if expression else "0")

    else:
        expression += str(value)
        display_var.set(expression)

# -----------------------------
# Button Creator
# -----------------------------
def create_btn(text, row, col, bg, fg="white", colspan=1):
    btn = tk.Button(
        root,
        text=text,
        font=("Helvetica", 22),
        bg=bg,
        fg=fg,
        bd=0,
        activebackground=bg,
        activeforeground=fg,
        relief="flat",
        command=lambda t=text: press(t)
    )
    btn.place(
        x=10 + col * 85,
        y=130 + row * 85,
        width=80 * colspan + (colspan - 1) * 5,
        height=80
    )

# -----------------------------
# Colors
# -----------------------------
gray = "#A5A5A5"
dark = "#333333"
orange = "#FF9500"

# -----------------------------
# Buttons Layout
# -----------------------------
buttons = [
    ("C", 0, 0, gray, "black"),
    ("⌫", 0, 1, gray, "black"),
    ("%", 0, 2, gray, "black"),
    ("/", 0, 3, orange),

    ("7", 1, 0, dark),
    ("8", 1, 1, dark),
    ("9", 1, 2, dark),
    ("*", 1, 3, orange),

    ("4", 2, 0, dark),
    ("5", 2, 1, dark),
    ("6", 2, 2, dark),
    ("-", 2, 3, orange),

    ("1", 3, 0, dark),
    ("2", 3, 1, dark),
    ("3", 3, 2, dark),
    ("+", 3, 3, orange),

    ("0", 4, 0, dark, "white", 2),
    (".", 4, 2, dark),
    ("=", 4, 3, orange),
]

for btn in buttons:
    if len(btn) == 6:
        create_btn(*btn)
    else:
        create_btn(*btn, colspan=1)

root.mainloop()