"""Caesar cipher"""
import string


def enter_key(alfabet):
    """Enter key to Caesar cipher"""
    key = input('Enter key to Caesar cipher: ')
    while not key.isdigit():
        key = input('Key to Caesar cipher can be only digits. Try again: ')
    key = int(key)
    while not key < len(alfabet) and key > 0:
        key = int(input(f'The key is out of range {len(alfabet)} of our alfabet. Try again: '))
    return key


def chek_input_massage(original_message, lanuage, alfabet):
    """Input validation"""
    try:
        cript_massage(original_message, lanuage)
    except KeyError:
        print(f'The message uses characters are not in the allowed alphabet [{alfabet}].'
              f'\nRestart program and enter correct message.')
        exit()
    return False


def encription_language(alfabet, encryption_key):
    """Make dictionary for encripting massage, where key is original letter and value is encripted letter"""
    encrypted_alphabet = []
    for letter in range(len(alfabet)):
        letter = alfabet[encryption_key]
        encrypted_alphabet.append(letter)
        if encryption_key < len(alfabet)-1:
            encryption_key += 1
        else:
            encryption_key -= encryption_key
    encription_language = dict(zip(list(alfabet), encrypted_alphabet))
    encription_language[' '] = ' '
    return encription_language


def decription_language(alfabet, decryption_key):
    """Make dictionary for encripting massage, where key is decripted letter and value is original letter"""
    decrypted_alphabet = []
    for letter in range(len(alfabet)):
        letter = alfabet[decryption_key]
        decrypted_alphabet.append(letter)
        if decryption_key < len(alfabet)-1:
            decryption_key += 1
        else:
            decryption_key -= decryption_key
    decription_language = dict(zip(decrypted_alphabet, list(alfabet)))
    decription_language[' '] = ' '
    return decription_language


def cript_massage(original_message, lanuage):
    """Read incoming massage and return the encripted or decripted one"""
    original_message = original_message.lower()
    cripted_massage = []
    for letter in original_message:
        cripted_massage.append(lanuage[letter])
    return ''.join(cripted_massage).capitalize()


def main(alfabet):
    """Main controller"""
    cryption_key = enter_key(alfabet)
    option = int(input("Do you want encript or decript your message? Enter:\n1 - encript\n2 - decript\nEnter: "))
    if option == 1:
        lanuage = encription_language(alfabet, cryption_key)
        original_message = input("Enter massage to encripting Caesar cipher: ")
        chek_input_massage(original_message, lanuage, alfabet)
        outgoing_message = cript_massage(original_message, lanuage)
    elif option == 2:
        lanuage = decription_language(alfabet, cryption_key)
        original_message = input("Enter massage to decripting Caesar cipher: ")
        chek_input_massage(original_message, lanuage, alfabet)
        outgoing_message = cript_massage(original_message, lanuage)
    else:
        print("You can choose only between 1 or 2. Try again.")
        exit()
    return outgoing_message


if __name__ == '__main__':
    alfabet = string.ascii_lowercase
    print(main(alfabet))
