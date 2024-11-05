#!/usr/bin/python3
"""
    The N queens puzzle is the challenge of placing N non-attacking queens
    on an N×N chessboard. This program solves the N queens problem.
"""


import sys


def print_solution(solution):
    """Print the list of queen positions as [row, col]."""
    print(solution)


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check column and diagonals for conflicts
    for i in range(row):
        if board[i] == col or \
           abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(board, row, N, solutions):
    """Use backtracking to solve the N Queens problem."""
    if row == N:
        # Solution found, store it in the solutions list
        solution = [[i, board[i]] for i in range(N)]
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            # Place queen
            board[row] = col
            solve_nqueens(board, row + 1, N, solutions)
            # Backtrack (not really needed because we just assign a value)
            board[row] = -1


def nqueens(N):
    """Solve the N Queens problem and print all solutions in
    the required format.
    """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    """Initialize the board, where board[i] is the column position
    of the queen in row i
    """
    board = [-1] * N
    solutions = []

    solve_nqueens(board, 0, N, solutions)

    for solution in solutions:
        print_solution(solution)


def main():
    """Main entry point to the program."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)


if __name__ == '__main__':
    main()
