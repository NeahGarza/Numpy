# REPL in command prompt opens Python's interactive mode
# If numpy module not found, run program in terminal
# Click empty space, then Run python file in terminal

import numpy as np

integers = np.array([1, 2, 3])

print(type(integers))
print(integers)


# LIST COMPREHENSION
integers = np.array([x for x in range(2, 21, 2)])
print(integers)

# make sure to include overal [] for entire list
integers = np.array([[1, 2, 3], [4, 5, 6]])
print(integers)

floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
print(floats)
