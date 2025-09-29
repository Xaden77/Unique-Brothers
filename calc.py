import tkinter as tk

class Calculator(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("Calculator")
        self.geometry("300x400")

        self.expression = ""  # stores what the user types
        self.entry = tk.Entry(self, width=20, font=("Arial", 18))
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
            ("=", 5, 0, 4)  # span across 4 columns
        ]

        for btn in buttons:
            text, row, col, *span = btn
            colspan = span[0] if span else 1
            button = tk.Button(self, text=text, width=5, height=2, font=("Arial", 14),
                               command=lambda t=text: self.on_click(t))
            button.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)

    def on_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.expression = result
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""
        elif char == "C":
            self.expression = ""
            self.entry.delete(0, tk.END)
        else:
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)




