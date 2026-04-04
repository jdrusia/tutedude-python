# Assignment 6: Calculator using tkinter

# importing the tkinter module
import tkinter as tk
import re


# Define the CalculatorApp class
class CalculatorApp:
    zero_division_error = "Zero Division Error"
    invalid_expression = "Invalid Expression"
    invalid_operator = "Invalid Operator"
    error = "Error"

    def __init__(self, root: tk.Tk):
        self.root = root

        # screen details
        self.root.title("Calculator")
        self.root.geometry("300x400")

        # expression variable to keep the current input/calculation
        self.expression = tk.StringVar(value="")

        # display entry to show input/output value
        self.display = tk.Entry(
            root, textvariable=self.expression, justify="right", font=("", 20)
        )

        # using grid layout for better organization
        # it places the display at row 0, and column 0, takes 4 columns
        # "nsew" sticky makes expand in all directions
        self.display.grid(row=0, column=0, columnspan=4, padx=2, pady=12, sticky="nsew")

        # layout of Calculator keypad
        layout = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("C", "0", "=", "+"),
        ]

        # create buttons one by one as in the layout
        for ridx, row in enumerate(layout, start=1):
            for cidx, label in enumerate(row):
                self.button(label, ridx, cidx)

        # used google to find this out
        # this makes columns and rows expand equally
        # when the window is resized
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)

        # bind Enter to evaluate
        self.root.bind("<Return>", lambda _: self.evaluate())

        # bind Escape to clear
        self.root.bind("<Escape>", lambda _: self.clear())

    def insert(self, string: str):
        # get current value and append it with new string and set it
        current = self.expression.get()

        # if curret value has error first clear it and then insert
        if current in [
            self.zero_division_error,
            self.invalid_expression,
            self.invalid_operator,
            self.error,
        ]:
            current = ""

        # if current has last value operator and string is also operator
        # then replace the operator
        if current and current[-1] in "+-*/" and string in "+-*/":
            current = current[:-1]

        # if current is 0 than clear to avoid leading zeros
        if current == "0" and string in "0123456789":
            current = ""

        # if operator is followed by 0 then remove the 0 to avoid leading zeros
        if (
            current
            and len(current) >= 2
            and current[-2] in "+-*/"
            and current[-1] == "0"
            and string in "0123456789"
        ):
            current = current[:-1]

        # finally appent th string to current
        final = current + string

        # if final has only + or * / operator then clear it
        if final in "+*/":
            final = ""

        # set the final value to expression
        self.expression.set(final)

    def button(self, text: str, row: int, col: int):
        # if = pressed the commad is evaluate,
        if text == "=":
            cmd = self.evaluate
        # if C pressed command is clear,
        elif text == "C":
            cmd = self.clear
        # else insert the text using lambda to pass test as argument to insert function
        else:
            cmd = lambda t=text: self.insert(t)

        btn = tk.Button(
            self.root, text=text, command=cmd, height=2, width=5, font=("", 18)
        )
        btn.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")

    def apply_operator(self, a, b, operator):
        # function to apply the operator
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            return a / b

    def evaluate_helper(self, _list, operator, idx):
        # helper function to apply the operator and return the modified list
        result = None
        if operator == "/":
            if _list[idx + 1] == "0":
                raise ZeroDivisionError
            result = self.apply_operator(
                float(_list[idx - 1]), float(_list[idx + 1]), "/"
            )
        elif operator == "*":
            result = self.apply_operator(
                float(_list[idx - 1]), float(_list[idx + 1]), "*"
            )
        elif operator == "+":
            result = self.apply_operator(
                float(_list[idx - 1]), float(_list[idx + 1]), "+"
            )
        elif operator == "-":
            result = self.apply_operator(
                float(_list[idx - 1]), float(_list[idx + 1]), "-"
            )
        else:
            # if invalid operator is passed
            raise ValueError(self.invalid_operator)

        # modify the list, replace the operator and two operands with the result
        # create a list with elements before the left operand, and append result
        new_list = _list[: idx - 1] + [str(result)]

        # if there are elements after the right operand, append them
        if idx + 2 < len(_list):
            new_list = new_list + _list[idx + 2 :]

        return new_list

    def evaluate(self):

        try:
            # get the current expression
            current = self.expression.get()

            # use regex to split the expression into numbers and operators
            _list = re.findall(r"\d+[.]?\d*|[+\-*\/]", current)

            # if empty return
            if not _list:
                return

            # only one element, then return
            if len(_list) == 1:
                return

            # if initial operator is + or - then combine it with the 2nd element
            if _list[0] in ["-", "+"]:
                _list = [f"{_list[0]}{_list[1]}"] + _list[2:]

            # run loop till only on element, result, is left
            while len(_list) > 1:
                # find the operators index in the precedence order and evaluate
                if "/" in _list:
                    idx = _list.index("/")
                    _list = self.evaluate_helper(_list, "/", idx)

                elif "*" in _list:
                    idx = _list.index("*")
                    _list = self.evaluate_helper(_list, "*", idx)

                elif "+" in _list:
                    idx = _list.index("+")
                    _list = self.evaluate_helper(_list, "+", idx)

                elif "-" in _list:
                    idx = _list.index("-")
                    _list = self.evaluate_helper(_list, "-", idx)

            result = float(_list[0])

            # if the result type is float and  it is integer, convert it to int to remove decimal
            if type(result) == float and result.is_integer():
                result = int(result)

            self.expression.set(str(result))

        except ZeroDivisionError:
            # if division by zero then show error
            self.expression.set(self.zero_division_error)
        except ValueError as e:
            # if invalid operator is used, show error
            self.expression.set(str(e))
        except:
            # for other errors, show Error
            self.expression.set(self.error)

    # Not being used
    def evaluate_eval(self):
        # use eval to evaluate the expression
        try:
            # get the value and eval it
            current = self.expression.get()
            result = eval(current)

            # if the result type is float and  it is integer, convert it to int to remove decimal
            if type(result) == float and result.is_integer():
                result = int(result)
            self.expression.set(str(result))
        except ZeroDivisionError:
            # if division by zero then show error
            self.expression.set(self.zero_division_error)
        except:
            # for other errors, show Error
            self.expression.set(self.error)

    def clear(self):
        self.expression.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
