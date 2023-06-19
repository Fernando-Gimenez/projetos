import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.result = tk.Entry(master, width=20, font=("Arial", 16))
        self.result.grid(row=0, column=0, columnspan=5)

        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("=", 4, 2)
        self.create_button("+", 4, 3)

        self.create_button("C", 5, 0, colspan=2)
        self.create_button("Sair", 5, 2, colspan=2)

    def create_button(self, text, row, column, colspan=1, rowspan=1):
        button = tk.Button(self.master, text=text, width=5, height=2, font=("Arial", 12),
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=column, columnspan=colspan, rowspan=rowspan)

    def button_click(self, text):
        if text == "C":
            self.result.delete(0, tk.END)
        elif text == "=":
            self.calculate()
        elif text == "Sair":
            self.master.quit()
        else:
            self.result.insert(tk.END, text)

    def calculate(self):
        try:
            result = eval(self.result.get())
            self.result.delete(0, tk.END)
            self.result.insert(tk.END, result)
        except:
            self.result.delete(0, tk.END)
            self.result.insert(tk.END, "Erro")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()

