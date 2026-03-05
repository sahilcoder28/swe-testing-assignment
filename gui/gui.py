import tkinter as tk


class CalculatorGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Quick-Calc")

        # Allow window resize
        root.geometry("400x550")

        self.expression = ""

        # Configure grid to expand
        for i in range(5):
            root.rowconfigure(i, weight=1)

        for i in range(4):
            root.columnconfigure(i, weight=1)

        # Display
        self.display = tk.Entry(
            root,
            font=("Arial", 32),
            bg="black",
            fg="white",
            justify="right",
            bd=10
        )

        self.display.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky="nsew",
            padx=10,
            pady=10
        )

        buttons = [

            ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
            ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
            ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
            ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3),

        ]

        for (text,row,col) in buttons:
            self.create_button(text,row,col)

    def create_button(self,text,row,col):

        button = tk.Button(
            self.root,
            text=text,
            font=("Arial",20),
            command=lambda:self.click(text)
        )

        button.grid(
            row=row,
            column=col,
            sticky="nsew",
            padx=5,
            pady=5
        )

    def click(self,char):

        if char == "C":

            self.expression = ""
            self.display.delete(0,tk.END)

        elif char == "=":

            try:

                result = str(eval(self.expression))

                self.display.delete(0,tk.END)
                self.display.insert(0,result)

                self.expression = result

            except:

                self.display.delete(0,tk.END)
                self.display.insert(0,"Error")

                self.expression = ""

        else:

            self.expression += str(char)

            self.display.delete(0,tk.END)
            self.display.insert(0,self.expression)


if __name__ == "__main__":

    root = tk.Tk()
    CalculatorGUI(root)
    root.mainloop()