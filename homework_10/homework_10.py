"""Typing on an old mobile"""
import re


def user_input():
    """Enter user message"""
    income_message = input("Enter your message: ").upper()
    outgoing_message = list(re.sub(r'[#;$%&*+@/=^_`{|}~-]', r'', income_message))
    return outgoing_message


def keystroke(user_input, keyboard):
    """Finding combination of button to typing your message"""
    typing = []
    for simbol in user_input:
        counter = 0
        while counter <= max(keyboard.keys()):
            if simbol in keyboard[counter]:
                typing.append(int(keyboard[counter].index(simbol) + 1) * str(counter))
            counter += 1
    return ''.join(typing)


def main(keyboard):
    """Main controller"""
    message = user_input()
    result = keystroke(message, keyboard)
    return result


if __name__ == '__main__':
    keyboard = {
        0: ' ',
        1: '.,?!:',
        2: 'ABC',
        3: 'DEF',
        4: 'GHI',
        5: 'JKL',
        6: 'MNO',
        7: 'PQRS',
        8: 'TUV',
        9: 'WXYZ'
    }
    result = main(keyboard)
    print(result)