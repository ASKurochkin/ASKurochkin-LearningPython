"""Vertical permutation cipher"""
import re


def rectangular_table(original_message: str, key_length: int):
    """Splitting the message into table of horizontal lines by key"""
    table_letters = []
    original_letters = "".join(str(original_message).split()).lower()
    while len(original_letters) % key_length:
        original_letters = original_letters + ' '
    start = 0
    finish = key_length
    for index, letter in enumerate(original_letters):
        if index < (len(original_letters) / key_length):
            table_letters.append(original_letters[start:finish])
            start += key_length
            finish += key_length
    return table_letters


def vertical_columns(rectangular_table: list, key_length: int):
    """Selecting vertical columns from a table of horizontal lines"""
    table_letters = []
    column_letters = []
    counter = 0
    while counter < key_length:
        for word in rectangular_table:
            table_letters.append(word[counter])
        counter += 1
    start = 0
    finish = int(len(table_letters) / key_length)
    for index, letter in enumerate(table_letters):
        if index < (len(table_letters) / (len(table_letters) / key_length)):
            column_letters.append(table_letters[start:finish])
            start += int(len(table_letters) / key_length)
            finish += int(len(table_letters) / key_length)
    return column_letters


def encrypt_message(vertical_columns: list, key_subsequence: list):
    """Collect columns in order of key values"""
    message = []
    sketch = dict(sorted(dict(zip(key_subsequence, vertical_columns)).items()))
    for number, cipher in sketch.items():
        message.append(cipher)
    return message


def message_output(encrypt_message: list):
    """Processing the message for output"""
    outgoing_message = []
    for part in encrypt_message:
        for letter in part:
            outgoing_message.append(letter)
    return re.sub(' ', '', ''.join(outgoing_message))


def main(original_message: str, key_length: int, key_subsequence: list):
    """Main controller"""
    lines = rectangular_table(original_message, key_length)
    columns = vertical_columns(lines, key_length)
    encrypted_message = encrypt_message(columns, key_subsequence)
    output = message_output(encrypted_message)
    return output


if __name__ == '__main__':
    original_message = 'Eat more of those soft french buns'
    key_subsequence = [3, 1, 4, 2, 5]
    key_length = len(key_subsequence)
    print(main(original_message, key_length, key_subsequence))