# def check_enter(number):
#     while type(number) != int:
#         print('You can only input numbers')
#         number = input()
#     return int(number)


def my_lists(first, last):
    for number in range(first, last + 1):
        first_lists.append(number)
    for n in first_lists:
        examination = list(map(int, str(n)))
        sum_list = []
        for index, item in enumerate(examination):
            value = item ** (index + 1)
            sum_list.append(value)
        result = sum(sum_list)
        if result == first_lists[n-1]:
             final_list.append(result)
    return (final_list)


first = int(input(f"Enter the first number: "))
last = int(input(f"Enter the last number: "))
first_lists = []
final_list = []

print(my_lists(first, last))