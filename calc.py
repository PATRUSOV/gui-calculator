import tkinter as tk

from src.operators.invocation import OperatorInvoker


root = tk.Tk()
root.geometry("500x600")
root.title("Calc")

entr_frame = tk.Frame(root, height=400, width=300)
entr_frame.place(anchor="center", relx=0.5, rely=0.5)

first_arg_entr = tk.Entry(entr_frame, justify="center")
first_arg_entr.place(relx=0.2, rely=0.5, anchor="center", width=100, height=40)
action_entr = tk.Entry(entr_frame, justify="center")
action_entr.place(relx=0.5, rely=0.5, anchor="center", width=30, height=30)
second_arg_entr = tk.Entry(entr_frame, justify="center")
second_arg_entr.place(relx=0.8, rely=0.5, anchor="center", width=100, height=40)


def make_window(name: str, text: str, color: str):
    window = tk.Toplevel()
    window.title(name)
    window.geometry("200x120")

    label = tk.Label(window, text=text, font=("Arial", 14, "bold"), fg=color)
    label.place(relx=0.5, rely=0.4, anchor="center")
    button = tk.Button(
        window,
        text="ok",
        font=("Arial", 12, "bold"),
        command=window.destroy,
    )
    button.place(relx=0.5, rely=0.8, anchor="center")


class ArgumentsProvider:
    def __init__(self, entr1: tk.Entry, entr2: tk.Entry):
        self.btn1 = entr1
        self.btn2 = entr2

    def get_args(self) -> tuple[int, int]:
        arg0 = int(self.btn1.get())
        arg1 = int(self.btn2.get())

        return arg0, arg1


class ActionProvider:
    def __init__(self, action_entr: tk.Entry):
        self._action_entry = action_entr

    def get_action(self) -> str:
        return self._action_entry.get().strip()


class Calculator:
    def __init__(self, args_prvdr: ArgumentsProvider, actn_prvdr: ActionProvider):
        self._args_prvdr = args_prvdr
        self._actn_prvdr = actn_prvdr

    def compute(self):
        try:
            actn_sym = self._actn_prvdr.get_action()
            arg0, arg1 = self._args_prvdr.get_args()
            result = OperatorInvoker.compute(actn_sym, arg0, arg1)
        except Exception as e:
            make_window("Error!", f"Error: {e}", "red")
        else:
            make_window("Answer", f"Answer: {result}", "green")


calculator = Calculator(
    ArgumentsProvider(first_arg_entr, second_arg_entr),
    ActionProvider(action_entr),
)


click_btn = tk.Button(root, text="Calculate", command=calculator.compute)
click_btn.place(anchor="center", relx=0.5, rely=0.6)


root.mainloop()
