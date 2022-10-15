"""Simulation dice thrown"""
import collections
from random import randint
from itertools import zip_longest
from prettytable import PrettyTable


def dice_are_thrown():
    """Simulation 1000 thrown of dice"""
    result = []
    for thrown in range(1000):
        first_result = randint(1, 6)
        second_result = randint(1, 6)
        result.append(first_result + second_result)
    return result


def range_of_probabilities():
    probabilities = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    probabilities_percent = []
    for dice in probabilities:
        dice = round(dice / 36 * 100, 1)
        probabilities_percent.append(dice)
    return probabilities_percent


def drop_frequency(dice_are_thrown):
    """Save all results with the frequency of their occurrence"""
    unique_results = collections.defaultdict(int)
    for result in dice_are_thrown:
        unique_results[result] += 1
    sort_unique_results = sorted(unique_results.items(), key=lambda x: x[0], reverse=False)
    return sort_unique_results


def drop_chance(drop_frequency, range_of_probabilities):
    """Calculate and collect the results of throws and the probabilities of getting combinations of numbers on dice"""
    chance = []
    for result, amount in drop_frequency:
        chance.append(result)
        chance.append(round((amount / 1000 * 100), 2))
    index = 2
    for value in range_of_probabilities:
        chance.insert(index, value)
        index += 3
    i_ = iter(chance)
    result_drops = list(zip_longest(i_, i_, i_))
    return result_drops


def table_of_drops(drop_chance):
    """Make table probability of 1000 thrown of dice"""
    table = PrettyTable()
    table.field_names = ['Exodus', 'Simulation percentage', 'Expected percentage']
    table.add_rows(drop_chance)
    return table


def main():
    """Main controller"""
    result_of_thrown = dice_are_thrown()
    result_frequency = drop_frequency(result_of_thrown)
    drop_probabilities = range_of_probabilities()
    drops = drop_chance(result_frequency, drop_probabilities)
    result_table = table_of_drops(drops)
    return result_table


if __name__ == '__main__':
    result = main()
    print(result)

