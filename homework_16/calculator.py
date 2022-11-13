"""My own calculator"""
from tkinter import *


class Calculator(Tk):
    """Main class to work with calculator"""
    def __init__(self):
        super().__init__()
        self.geometry("410x290")
        self.title('CALCULATOR')
        self.config(background='#1c1c1c')

        self.result_field = ResultField()

        self.button_1 = PushButton('1', 4, 1)
        self.button_2 = PushButton('2', 4, 2)
        self.button_3 = PushButton('3', 4, 3)
        self.button_4 = PushButton('4', 3, 1)
        self.button_5 = PushButton('5', 3, 2)
        self.button_6 = PushButton('6', 3, 3)
        self.button_7 = PushButton('7', 2, 1)
        self.button_8 = PushButton('8', 2, 2)
        self.button_9 = PushButton('9', 2, 3)
        self.button_0 = PushButton('0', 5, 1)
        self.button_00 = PushButton('00', 5, 2)
        self.button_dot = PushButton('.', 5, 3)
        self.button_divide = PushButton('/', 2, 4)
        self.button_mult = PushButton('*', 3, 4)
        self.button_plus = PushButton('+', 4, 4)
        self.button_plus = PushButton('-', 5, 4)
        self.button_plus = PushButton('**2', 4, 5)
        self.button_plus = PushButton('**(1/2)', 3, 5)
        self.button_equal = ButtonEqual('=', 5, 5)
        self.button_AC = ButtonClear('CLEAR', 2, 5)


class PushButton:
    """All buttons that add the character written on the button"""
    __height = 2
    __width = 4

    def __init__(self, char: str, row: int, column: int):
        super().__init__()
        self.button = Button(text=char, height=self.__height, width=self.__width,
                             command=lambda: ResultField().press_button(char))
        self.button.grid(row=row, column=column)


class ButtonEqual:
    """Buttons equal"""
    __height = 2
    __width = 4

    def __init__(self, char: str, row: int, column: int):
        super().__init__()
        self.button = Button(text=char, height=self.__height, width=self.__width,
                             command=lambda: ResultField().press_equal())
        self.button.grid(row=row, column=column)


class ButtonClear:
    """Button for clear Entry and reset operation"""
    __height = 2
    __width = 4

    def __init__(self, char: str, row: int, column: int):
        super().__init__()
        self.button = Button(text=char, height=self.__height, width=self.__width,
                             command=lambda: ResultField().clear_result())
        self.button.grid(row=row, column=column)


class ResultField:
    """Calculator screen"""
    __background = 'gray'
    __font = ('Ubuntu Mono', 25, 'bold')

    def __init__(self):
        super().__init__()
        self.result = StringVar()
        self.field = Entry(background=self.__background, font=self.__font, textvariable=self.result)
        self.field.grid(columnspan=6, ipadx=30, pady=10)

    def press_button(self, button):
        global enter
        enter += str(button)
        self.result.set(enter)

    def press_equal(self):
        try:
            global enter
            calculation = str(eval(enter))
            self.result.set(calculation)
            enter = calculation
        except:
            self.result.set("Error")

    def clear_result(self):
        global enter
        calculation = ''
        self.result.set(calculation)
        enter = calculation


if __name__ == '__main__':
    enter = ''
    calculator = Calculator()
    calculator.mainloop()
