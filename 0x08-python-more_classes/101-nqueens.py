#!/usr/bin/python3
"""
This program solves the N queens puzzle.
The N queens puzzle is the challenge of placing N non-
attacking queens on an NxN chessboars
"""
import sys


def check_horizontally(cell, solution):
    a = cell[0]
    while not (a < 0):
        if [a, cell[1]] in solution:
            return False
        a -= 1
    return True


def check_diagonally_up(cell, solution, N):
    a = cell[0]
    b = cell[1]
    while (a >= 0) and (b < N):
        if [a, b] in solution:
            return False
        a -= 1
        b += 1
    return True


def check_diagonally_down(cell, solution):
    a = cell[0]
    b = cell[1]
    while (a >= 0) and (b >= 0):
        if [a, b] in solution:
            return False
        a -= 1
        b -= 1
    return True


def nqueens_recursive(row, N, partial_solution, solution):
    if row == N:
        solution.append(partial_solution[:])
        return

    for col in range(N):
        cell = [row, col]
        if (check_horizontally(cell, partial_solution)
                and check_diagonally_up(cell, partial_solution, N)
                and check_diagonally_down(cell, partial_solution)):
            partial_solution.append(cell)
            nqueens_recursive(row + 1, N, partial_solution, solution)
            partial_solution.pop()


def nqueens(N):
    solution = []
    nqueens_recursive(0, N, [], solution)
    return solution


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: nqueens N")
        exit(1)
    if type(sys.argv[1]) is not int:
        print("N must be a number")
        exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)
    solution = nqueens(N)
    for sol in solution:
        print(sol)
