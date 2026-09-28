import matplotlib.pyplot as plt
import numpy as np

first = np.array([1, 2, 3, 4, 5])
second = np.zeros(5)
third = np.arange(0, 10, 2)
fourth = np.linspace(0, 1, 5)

print(first)
print(second)
print(third)
print(fourth)

fifth = np.reshape(first, (5, 1))
print(fifth)

sixth = np.concatenate((first, second), axis=0)
print(sixth)