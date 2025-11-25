import numpy as np
import timeit

# Vectorized sum
print(np.sum(np.arange(4)))
print("Time taken by vectorized sum:", end=" ")
print(timeit.timeit("np.sum(np.arange(4))", setup="import numpy as np", number=100000))

# Iterative sum
total = 0
for item in range(0, 4):
    total += item
a = total
print("\n" + str(a))
print("Time taken by iterative sum:", end=" ")
print(timeit.timeit("""
total = 0
for item in range(0, 4):
    total += item
""", number=100000))