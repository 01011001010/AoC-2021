from statistics import median


def cost(n):
    return n*(1+n)//2


with open('7.txt', 'r') as file:
    numbers = list(map(int, file.read().strip().split(',')))
med = round(median(numbers))
ave = sum(numbers)//len(numbers)

print('Part 1:', sum(map(lambda x: abs(x-med), numbers)))
print('Part 2:', sum(map(lambda x: cost(abs(x-ave)), numbers)))
