import math

def read_input():
    with open('day1_input.txt','r') as input:
        lines = input.readlines()
    return lines   


def calculate_fuel_total(modules):
    value = 0
    for module in modules:
        value += _calculate_fuel(module)
    return value


def _calculate_fuel(module):
    fuel = math.floor(int(module)/3) - 2
    if (math.floor(int(fuel)/3) - 2 > 0):
        fuel += _calculate_fuel(fuel)
    return fuel


if __name__ == "__main__":
    modules = read_input()
    print(calculate_fuel_total(modules))
