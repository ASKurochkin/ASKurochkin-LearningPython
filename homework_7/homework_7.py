import os
import re


def examination(our_data):
    """Input validation"""
    try:
        open(our_data).readline()
    except UnicodeDecodeError:
        print('Need use only text files format')
        exit()
    except FileNotFoundError as error:
        print(error)
        exit()


def mendeleev_table(our_text):
    """Delete digits, clear sings and create periodic table dictionary """
    with open(our_text) as file:
        mendel_string = []
        mendel_table = {}
        for line in file:
            cleared_digit = re.sub('[\d\n]', '', line)
            cleared_signs = re.sub('[\W]', ' ', cleared_digit)
            mendel_string.append(cleared_signs)
            for index, value in enumerate(mendel_string):
                mendel_table[index + 1] = value
    return mendel_table


def check_input_data(user_data):
    """Checking user data for digit format and valid range"""
    while user_data.isdigit() == False:
        user_data = input(f'You can enter only digits. Try again: ')
        return int(user_data)
    check_numbers = []
    for index in mendeleev_table(our_file):
        check_numbers.append(index)
    while int(user_data) not in range(min(check_numbers), max(check_numbers)):
        user_data = input(
            f"You can enter only the number of chemical elements of the periodic table between {min(check_numbers)} and {max(check_numbers)}"
            f"\n Try again: ")
        return int(user_data)
    return int(user_data)


def exit_program(user_data):
    """Exit program if user leave the field blank"""
    if user_data == '':
        print("The program has been closed. Thanks for using")
        exit()
    return (check_input_data(user_data))


if __name__ == '__main__':
    current_dir = os.getcwd()
    our_file = os.path.join(current_dir, 'elements.txt')
    while True:
        chemical_number = exit_program(
            input(f"Enter the number of the chemical element of the Mendeleev periodic system: "))
        if chemical_number == None:
            break
        print(f'Chemical element is{mendeleev_table(our_file)[chemical_number]} and it have {chemical_number} protons')
