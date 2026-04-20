import tkinter as tk
import ast
import operator as op

# Safe operators for the calculator
_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.USub: op.neg,
}


def _safe_eval(node):
    """Recursively evaluate an AST node using only safe numeric operators."""
    if isinstance(node, ast.Expression):
        return _safe_eval(node.body)
    elif isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    elif isinstance(node, ast.BinOp) and type(node.op) in _OPERATORS:
        return _OPERATORS[type(node.op)](_safe_eval(node.left), _safe_eval(node.right))
    elif isinstance(node, ast.UnaryOp) and type(node.op) in _OPERATORS:
        return _OPERATORS[type(node.op)](_safe_eval(node.operand))
    else:
        raise ValueError("Unsupported expression")


def safe_calculate(expression: str) -> str:
    try:
        tree = ast.parse(expression, mode='eval')
        result = _safe_eval(tree)
        # Return integer string if result is whole number
        return str(int(result)) if result == int(result) else str(result)
    except Exception:
        return "Error"


class Calculator(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("Calculator")
        self.geometry("300x400")

        self.expression = ""
        self.entry = tk.Entry(self, width=20, font=("Arial", 18))
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
            ("=", 5, 0, 4),
        ]

        for btn in buttons:
            text, row, col, *span = btn
            colspan = span[0] if span else 1
            button = tk.Button(
                self, text=text, width=5, height=2, font=("Arial", 14),
                command=lambda t=text: self.on_click(t),
            )
            button.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)

    def on_click(self, char):
        if char == "=":
            result = safe_calculate(self.expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
            self.expression = result if result != "Error" else ""
        elif char == "C":
            self.expression = ""
            self.entry.delete(0, tk.END)
        else:
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)