import tkinter as tk
from tkinter import font


def add(a, b):
  return a + b


def subtract(a, b):
  return a - b


def multiply(a, b):
  return a * b


def divide(a, b):
  if b == 0:
    raise ValueError("Cannot divide by zero")
  return a / b


OPERATIONS = {
  "Add": ("+", add),
  "Subtract": ("−", subtract),
  "Multiply": ("×", multiply),
  "Divide": ("÷", divide),
}


class CalculatorApp:
  def __init__(self, root):
    self.root = root
    self.root.title("Calculator")
    self.root.geometry("320x520")
    self.root.resizable(False, False)
    self.root.configure(bg="#1c1c1c")

    self.display_var = tk.StringVar(value="0")
    self.stored_value = None
    self.pending_operation = None
    self.reset_input = False

    self._build_menu()
    self._build_display()
    self._build_buttons()
    self._bind_keys()

  def _build_menu(self):
    menu_bar = tk.Menu(self.root)
    operation_menu = tk.Menu(menu_bar, tearoff=0)
    for name, (symbol, _) in OPERATIONS.items():
      operation_menu.add_command(
        label=f"{name} ({symbol})",
        command=lambda s=symbol: self.set_operation(s),
      )
    menu_bar.add_cascade(label="Operations", menu=operation_menu)
    self.root.config(menu=menu_bar)

  def _build_display(self):
    display_frame = tk.Frame(self.root, bg="#1c1c1c", padx=12, pady=12)
    display_frame.pack(fill="x")

    display_font = font.Font(family="Segoe UI", size=36, weight="bold")
    self.display = tk.Label(
      display_frame,
      textvariable=self.display_var,
      anchor="e",
      bg="#1c1c1c",
      fg="#ffffff",
      font=display_font,
      padx=8,
      pady=16,
    )
    self.display.pack(fill="x")

  def _build_buttons(self):
    button_frame = tk.Frame(self.root, bg="#1c1c1c", padx=12, pady=8)
    button_frame.pack(fill="both", expand=True)

    buttons = [
      ("C", self.clear, "function"),
      ("⌫", self.backspace, "function"),
      ("±", self.toggle_sign, "function"),
      ("÷", lambda: self.set_operation("÷"), "operator"),
      ("7", lambda: self.append_digit("7"), "number"),
      ("8", lambda: self.append_digit("8"), "number"),
      ("9", lambda: self.append_digit("9"), "number"),
      ("×", lambda: self.set_operation("×"), "operator"),
      ("4", lambda: self.append_digit("4"), "number"),
      ("5", lambda: self.append_digit("5"), "number"),
      ("6", lambda: self.append_digit("6"), "number"),
      ("−", lambda: self.set_operation("−"), "operator"),
      ("1", lambda: self.append_digit("1"), "number"),
      ("2", lambda: self.append_digit("2"), "number"),
      ("3", lambda: self.append_digit("3"), "number"),
      ("+", lambda: self.set_operation("+"), "operator"),
      ("0", lambda: self.append_digit("0"), "number"),
      (".", self.append_decimal, "number"),
      ("=", self.calculate, "equals"),
    ]

    btn_font = font.Font(family="Segoe UI", size=18)

    for index, (text, command, style) in enumerate(buttons):
      row = index // 4
      column = index % 4
      column_span = 2 if text == "0" else 1

      if text == "0":
        column = 0
      elif text == ".":
        column = 2
      elif text == "=":
        column = 3

      colors = {
        "number": ("#333333", "#ffffff"),
        "operator": ("#ff9f0a", "#ffffff"),
        "function": ("#a5a5a5", "#000000"),
        "equals": ("#ff9f0a", "#ffffff"),
      }
      bg, fg = colors[style]

      tk.Button(
        button_frame,
        text=text,
        command=command,
        font=btn_font,
        bg=bg,
        fg=fg,
        activebackground=bg,
        activeforeground=fg,
        relief="flat",
        bd=0,
        width=5 if column_span == 1 else 11,
        height=2,
        cursor="hand2",
      ).grid(row=row, column=column, columnspan=column_span, padx=4, pady=4, sticky="nsew")

    for i in range(4):
      button_frame.grid_columnconfigure(i, weight=1)
    for i in range(5):
      button_frame.grid_rowconfigure(i, weight=1)

  def _bind_keys(self):
    for digit in "0123456789":
      self.root.bind(digit, lambda event, d=digit: self.append_digit(d))
    self.root.bind(".", lambda event: self.append_decimal())
    self.root.bind("+", lambda event: self.set_operation("+"))
    self.root.bind("-", lambda event: self.set_operation("−"))
    self.root.bind("*", lambda event: self.set_operation("×"))
    self.root.bind("/", lambda event: self.set_operation("÷"))
    self.root.bind("<Return>", lambda event: self.calculate())
    self.root.bind("=", lambda event: self.calculate())
    self.root.bind("<BackSpace>", lambda event: self.backspace())
    self.root.bind("<Escape>", lambda event: self.clear())

  def current_value(self):
    return float(self.display_var.get())

  def append_digit(self, digit):
    current = self.display_var.get()
    if self.reset_input or current == "Error":
      current = "0"
      self.reset_input = False

    if current == "0" and digit != ".":
      self.display_var.set(digit)
    else:
      self.display_var.set(current + digit)

  def append_decimal(self):
    current = self.display_var.get()
    if self.reset_input or current == "Error":
      self.display_var.set("0.")
      self.reset_input = False
      return
    if "." not in current:
      self.display_var.set(current + ".")

  def toggle_sign(self):
    current = self.display_var.get()
    if current == "Error" or current == "0":
      return
    if current.startswith("-"):
      self.display_var.set(current[1:])
    else:
      self.display_var.set("-" + current)

  def backspace(self):
    current = self.display_var.get()
    if current == "Error":
      self.clear()
      return
    if len(current) <= 1 or (current.startswith("-") and len(current) == 2):
      self.display_var.set("0")
    else:
      self.display_var.set(current[:-1])

  def clear(self):
    self.display_var.set("0")
    self.stored_value = None
    self.pending_operation = None
    self.reset_input = False

  def set_operation(self, symbol):
    if self.display_var.get() == "Error":
      return

    if self.stored_value is not None and self.pending_operation and not self.reset_input:
      self.calculate()

    self.stored_value = self.current_value()
    self.pending_operation = self._operation_for_symbol(symbol)
    self.reset_input = True

  def calculate(self):
    if self.pending_operation is None or self.stored_value is None:
      return

    try:
      result = self.pending_operation(self.stored_value, self.current_value())
      self.display_var.set(self._format_result(result))
      self.stored_value = None
      self.pending_operation = None
      self.reset_input = True
    except ValueError:
      self.display_var.set("Error")
      self.stored_value = None
      self.pending_operation = None
      self.reset_input = True

  def _operation_for_symbol(self, symbol):
    for _, (op_symbol, function) in OPERATIONS.items():
      if op_symbol == symbol:
        return function
    raise ValueError(f"Unknown operation: {symbol}")

  def _format_result(self, value):
    if value == int(value):
      return str(int(value))
    text = f"{value:.10f}".rstrip("0").rstrip(".")
    return text


def main():
  root = tk.Tk()
  CalculatorApp(root)
  root.mainloop()


if __name__ == "__main__":
  main()
