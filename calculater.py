import tkinter as tk
from math import sin, cos, tan, log, sqrt, radians, factorial

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator by CHANDAN")

        self.result = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.result, font=("Arial", 20), bd=10, insertwidth=12, width=42, borderwidth=12)
        self.entry.grid(row=0, column=0, columnspan=5)

        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', 'sin',
            '1', '2', '3', '-', 'cos',
            '0', '.', '+', '=', 'tan',
            '(', ')', 'sqrt', 'log', 'exp', 'factorial'
        ]

        row = 1
        col = 0

        for text in button_texts:
            if text not in {'sin', 'cos', 'tan', 'sqrt', 'log', 'exp', 'factorial'}:
                button = tk.Button(self.master, text=text, padx=20, pady=20, font=("Arial", 18),
                                   command=lambda t=text: self.on_button_click(t))
            else:
                button = tk.Button(self.master, text=text, padx=15, pady=20, font=("Arial", 18),
                                   command=lambda t=text: self.on_sci_button_click(t))
            button.grid(row=row, column=col)

            col += 1
            if col > 4:
                col = 0
                row += 1

    def on_button_click(self, char):
        if char == 'C':
            self.result.set("")
        elif char == '=':
            try:
                expression = self.result.get()
                self.result.set(eval(expression))
            except Exception as e:
                self.result.set("Error")
        else:
            current_text = self.result.get()
            self.result.set(current_text + str(char))

    def on_sci_button_click(self, func):
        try:
            current_text = self.result.get()

            if func == 'sin':
                value = str(sin(radians(float(current_text))))
            elif func == 'cos':
                value = str(cos(radians(float(current_text))))
            elif func == 'tan':
                value = str(tan(radians(float(current_text))))
            elif func == 'sqrt':
                value = str(sqrt(float(current_text)))
            elif func == 'log':
                value = str(log(float(current_text)))
            elif func == 'exp':
                value = str(float(current_text) ** 2)
            elif func == 'factorial':
                value = str(factorial(int(current_text)))
            self.result.set(value)
        except Exception as e:
            self.result.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
