import math
from collections import Counter

# Constants
values = [*range(1, 7)]  # List of possible values of a six-sided die

# Get number of spins from user
spins = max(int(input("How many spins? ")) - 1, 0)

# Calculate all possible sums from the specified number of spins
possibilities = values[:]
for _ in range(spins):
    possibilities = [result + oldSum for result in values for oldSum in possibilities]

# Calculate the number of significant figures needed to display each sum
significant_figures = math.ceil(math.log10(max(possibilities)))

# Count the frequency of occurrence of each sum and sort by frequency in descending order
sums_and_frequencies = [(value, frequency) for value, frequency in Counter(possibilities).most_common()]

# Print the results
for sum_and_frequency in sums_and_frequencies:
    value, frequency = sum_and_frequency
    print(f"Sum: {value:0{significant_figures}d} | Frequency: {frequency}")
print(len(possibilities))
