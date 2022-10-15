import os
import re

current_dir = os.getcwd()
our_text = os.path.join(current_dir, 'example.txt')

try:
    """Input validation"""
    open(our_text).readline()
except UnicodeDecodeError:
    print('Need use only text files format')
    exit()
except FileNotFoundError as error:
    print(error)
    exit()

def longest_words(text):
    with open(text) as file:
        for line in file:
            """Prepare a file for analysis"""
            line = line.strip()
            cleared_text = re.sub('[\,.()"":/]', '', line)
            divided_text = re.split(r'\W', cleared_text)
            """Find the longest word"""
            max_word = len(max(divided_text, key=len))
            print(f'Longest word(s) contains {max_word} characters')
            print('These word(s) is:')
            """Find and print words of the same length"""
            words = []
            for word in divided_text:
                if len(word) == max_word:
                    words.append(word)
            return(words)

print(longest_words(our_text))
