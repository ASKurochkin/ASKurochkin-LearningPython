import string
import re

name = 'Курочкин Александр Сергеевич'

if re.search(r'[01234567890]', name):
    print("Понял")
else:
    print("Не понял")
