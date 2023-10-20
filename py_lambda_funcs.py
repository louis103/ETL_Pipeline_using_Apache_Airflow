# lambda functions
squared = lambda num: num * num
print(squared(2))

addTwo = lambda num: num + 2
print(addTwo(5))

sum_total = lambda a, b: a + b
print(sum_total(2, 3))


####################
def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

# Higher order functions
# A function that takes oner or more functions as arguments or
# a function that returns a function as its result.

# Map

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers)
print(list(squared_nums))


#### Filter

odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_nums))


### Reduce
from functools import reduce


numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

total = reduce(lambda acc, curr: acc + curr, numbers2)
print(total)

# get sum using built-in sum
print(sum(numbers2, 20))


names = ["Louis", "Mary", "John", "Jingleheimerschmidst"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
