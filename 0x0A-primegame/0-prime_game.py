#!//bin/python3
"""Module for x num game"""


def isWinner(x, nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    wins_maria = 0
    wins_ben = 0

    for n in nums:
        prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))
        if prime_count % 2 == 0:
            wins_ben += 1
        else:
            wins_maria += 1

    if wins_maria > wins_ben:
        return "Maria"
    elif wins_ben > wins_maria:
        return "Ben"
    else:
        return None
