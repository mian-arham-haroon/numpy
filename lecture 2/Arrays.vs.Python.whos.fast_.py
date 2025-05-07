import timeit
import numpy as np

# Timing the NumPy operation
numpy_time = timeit.timeit(lambda: np.arange(1, 9) ** 4, number=100000)

# Timing the list comprehension
list_comp_time = timeit.timeit('[j**4 for j in range(1, 9)]', number=100000)

print(f"NumPy time: {numpy_time}")
print(f"List comprehension time: {list_comp_time}")
