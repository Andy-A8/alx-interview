#!/usr/bin/python3
"""
    Prime game
"""


def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """ Create a boolean list for primes up to n(True means prime) """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
        for i in range(2, int(n ** 0.5) + 1):
            if prime[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i in range(2, n + 1) if primes[i]]

    def simulate_game(n):
        """ Generate the list of primes up to n """
        primes = sieve_of_eratosthenes(n)
        available_numbers = [True] * (n + 1)
        player_turn = 0  # 0 for Maria, 1 for Ben

        while True:
            move = -1
            for p in primes:
                if p <= n and available_numbers[p]:
                    move = p
                    break

            if move == -1:
                return 1 - player_turn

            for multiple in range(move, n + 1, move):
                available_numbers[multiple] = False

            player_turn = 1 - player_turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = simulate_game(n)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
