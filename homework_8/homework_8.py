"""Finding the most used e:mail"""
import collections
import os
import re
from prettytable import PrettyTable


def path_to_file():
    """Get path to file with data"""
    current_dir = os.getcwd()
    filename = input("Enter text file name with extension (*.txt) for analysis: ")
    while not os.path.exists(filename):
        filename = input("You entered the name of a non-existent file. Try again: ")
        return filename
    our_file = os.path.join(current_dir, filename)
    return our_file


def chek_data(path_to_file: str):
    """Input validation"""
    try:
        open(path_to_file).readline()
    except UnicodeDecodeError:
        print('Need use only text files format')
        exit()
    except FileNotFoundError as error:
        print(error)
        exit()


def read_data_from_file(path_to_file: str):
    """Read data from txt file"""
    data = []
    with open(path_to_file) as file:
        for line in file:
            line = line.strip()
            data.append(line)
        return data


def finding_email(massive: list):
    """Extracting E-mail from text"""
    email = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9_.+-]+', str(massive))
    return sorted(email)


def separate_domain(finding_email: list):
    """Separate the domain from the user's mail"""
    flag_char = '@'
    domains = []
    for email in finding_email:
        char_index = email.find(flag_char)
        domain = email[char_index+1:]
        domains.append(domain)
    return domains


def domain_counter(separate_domain: list):
    """Let's count the number of unique domains"""
    numerated = collections.defaultdict(int)
    for domian in separate_domain:
        numerated[domian] +=1
    sort_numerated = sorted(numerated.items(), key=lambda x: x[1], reverse=True)
    return sort_numerated


def table_of_domian(domain_counter: list):
    """Make output table"""
    table = PrettyTable()
    table.field_names = ['Domain', 'Number of emails']
    table.add_rows(domain_counter)
    return table


def main(path_to_file: str):
    chek = chek_data(path_to_file)
    if chek:
        print(chek)
        exit()
    massive = read_data_from_file(path_to_file)
    email = finding_email(massive)
    domains = separate_domain(email)
    number_of_domains = domain_counter(domains)
    table = table_of_domian(number_of_domains)
    print(table)


if __name__ == '__main__':
    main(path_to_file())
