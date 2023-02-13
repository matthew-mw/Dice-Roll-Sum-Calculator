# Rolling a Six-Sided Die

This is a simple program that simulates the rolling of a six-sided die. The user inputs the number of spins they want to simulate and the program calculates the possible sums that can be obtained and their frequency of occurrence. The results are then printed in descending order of frequency.

## Prerequisites

To run this program, you must have Python 3 installed on your machine. You can download it from [Python.org](https://www.python.org).

## Installation

To install the program, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/matthew-mw/Dice-Roll-Sum-Calculator.git
```

2. Navigate to the directory where you cloned the repository:

```
cd Dice-Roll-Sum-Calculator
```

## Running the Program

To run the program, follow these steps:

1. Open a terminal and navigate to the directory where you cloned the repository.
2. Run the following command:

```
python3 dice_roll_sum_calculator.py
```

## Usage

1. The program will prompt you to enter the number of spins. 
2. Enter a number and press enter. 
3. The program will then calculate all possible sums and print a list of the sums and their frequencies.

## Built With

- Python 3

## Author

- Matthew Wang, the author of the program. You can find his GitHub profile [here](https://github.com/matthew-mw).

## Acknowledgments

- The program uses the `collections` module for counting the frequency of each sum.
- The `math` module is used for rounding up the logarithm of the maximum sum to the nearest integer.