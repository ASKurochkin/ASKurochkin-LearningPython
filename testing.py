keyboard = {
        0: 'ABC',
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
user_input = 'B'
typing = []
for simbol in user_input:
    if simbol in keyboard[0]:
        typing.append(int(keyboard[0].index(simbol)+1)*str(0))
print(typing)