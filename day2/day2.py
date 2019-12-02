
def read_input():
    with open('day2/input.txt', 'r') as f:
        return list(map(int,str(f.readline()).split(',')))

def calculate(list):
    for i, element in enumerate(list):
        if i == 0 or i % 4 == 0:
            if element == 99:
                return list
            else:
                list[list[i+3]] = _calculate_block(element, list[list[i+1]], list[list[i+2]])
        else:
            pass

def _calculate_block(operator, index1, index2):
    if operator == 1:
        return index1 + index2
    elif operator == 2:
        return index1 * index2

if __name__ == '__main__':
    list = read_input()
    print(calculate(list))