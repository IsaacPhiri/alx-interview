# Prime Game

This program implements the Prime Game, a game played by two players, Maria and Ben. In each round, the players take turns choosing a prime number from a given set of consecutive integers starting from 1 up to and including a specific number, `n`. The chosen prime number and its multiples are then removed from the set. The player who cannot make a move loses the game. This program determines the winner of each game session based on the number of rounds played.

## Algorithm Explanation

The algorithm used in the `isWinner` function follows these steps:

1. Initial checks are performed to ensure the validity of the input. If the number of rounds is less than 1 or the list of numbers is empty, the function returns `None`.

2. The maximum value of `n` is determined from the input list of numbers. This value represents the upper limit for generating prime numbers.

3. Prime numbers are generated using a sieve-like approach. A list is created with `n` elements, initialized to `True`. The first two elements, representing 0 and 1, are manually set to `False` since they are not prime. The remaining elements are marked as prime or non-prime based on their multiples.

4. The function plays each round of the game. For each round, the count of prime numbers less than or equal to `n` is determined using the generated list of prime numbers.

5. The number of wins for Maria and Ben is updated based on the parity of the prime count. If the count is even, Ben wins the round, and the corresponding counter is incremented. If the count is odd, Maria wins the round, and her counter is incremented.

6. Finally, the overall winner is determined by comparing the number of wins for Maria and Ben. If they are equal, it means the winner cannot be determined, and `None` is returned. Otherwise, the name of the player with the most wins is returned.

## Requirements

- Python version: 3.4.3
- Operating System: Ubuntu 14.04 LTS

## Usage

1. Ensure that you have Python 3.4.3 installed on your system.

2. Clone the repository and navigate to the project's root directory.

3. Open a terminal and execute the following command to run the program:
	```
	root@USER$ ./0-main.py
	```
4. Modify the `x` and `nums` variables in the `prime_game.py` file to customize the number of rounds and the list of numbers for each round.

5. The program will determine the winner of each game session based on the provided inputs and display the result.

## Limitations

- The algorithm can handle `x` rounds and numbers up to 10,000. Exceeding these limits may result in performance issues or incorrect results.

- The program does not validate the input values. It assumes that the input values are integers and within the specified limits.

- The program does not have any external dependencies. It is self-contained and uses only built-in Python libraries.

