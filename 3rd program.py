from functools import reduce
numbers = range(1, 101)
multiples_of_3 = list(filter(lambda x: x % 3 == 0, numbers))
print("Multiples of 3:", multiples_of_3)
squares = list(map(lambda x: x**2, multiples_of_3))
print("Squares of multiples of 3:", squares)
sum_multiples = reduce(lambda acc, x: acc + x, multiples_of_3, 0)
print("Sum of multiples of 3:", sum_multiples)
