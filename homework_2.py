# Encode the chessboard as strings
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [2, 3, 4, 5, 6, 7, 8, 9]
c = [1, 2, 3, 4, 5, 6, 7, 8]
d = [2, 3, 4, 5, 6, 7, 8, 9]
e = [1, 2, 3, 4, 5, 6, 7, 8]
f = [2, 3, 4, 5, 6, 7, 8, 9]
g = [1, 2, 3, 4, 5, 6, 7, 8]
h = [2, 3, 4, 5, 6, 7, 8, 9]

#Create conditions for checking valid values
def check_enter_hor(hor_line):
    while hor_line not in 'abcdefgh':
        print('You can only input letters from a to h')
        hor_line = input("Enter horizontal coordinate (for example:a-h):")
    return str(hor_line)
def check_enter_vert(vert_line):
    while vert_line not in '12345678':
        print('You can only input numbers from 1 to 8')
        vert_line = input("Enter vertical coordinate (for example:1-8):")
    return int(vert_line)

#Create a loop for the possibility of an infinite run
while True:
    print('You have a chessboard. Enter the coordinates of the square whose color you are interested in.')

#We will ask the user for the coordinates of the square
    horizontal_word = check_enter_hor(input("Enter horizontal coordinate (for example:a-h):").lower())
    vertikal = check_enter_vert(input("Enter vertical coordinate (for example:1-8):"))

# Transform horizontal coordinates from dictionary
    dick = {'a': a,
            'b': b,
            'c': c,
            'd': d,
            'e': e,
            'f': f,
            'g': g,
            'h': h
            }

    horizontal_variable = dick[horizontal_word]
    square = horizontal_variable[vertikal - 1]
    if square % 2 == 0:
        colour = str('white')
    else:
        colour = str('black')
    print(f"You chose a {colour} sqare")
    trying = input("Do you want to try again? (y/n)").lower()
    if trying == 'n':
        break
print("Thank you for your time. That's all.")
#And all is happy :)