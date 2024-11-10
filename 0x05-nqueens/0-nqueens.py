#!/usr/bin/python3
import sys


def print_usage():
    """Print usage instructions for the program."""
    print("Usage: nqueens N")


def validate_input(args):
    """
    Validate the input arguments.
    
    Args:
        args (list): The command-line arguments.
    
    Returns:
        int: The validated board size N.
    
    Raises:
        SystemExit: If the input is invalid, it exits the program with a status of 1.
    """
    if len(args) != 2:
        print_usage()
        sys.exit(1)
    try:
        n = int(args[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        return n
    except ValueError:
        print("N must be a number")
        sys.exit(1)


def is_safe(board, col):
    """
    Check if the current queen placement is safe.
    
    Args:
        board (list): Current state of the board.
        col (int): Column index of the queen.
    
    Returns:
        bool: True if the queen placement is safe, False otherwise.
    """
    for i in range(col):
        if board[col] == board[i] or abs(board[col] - board[i]) == col - i:
            return False
    return True


def solve_nqueens(n):
    """
    Solve the N Queens problem using backtracking.
    
    Args:
        n (int): The size of the chessboard (N x N).
    
    Returns:
        list: A list of all possible solutions, where each solution is a list
              of positions [row, col] for each queen on the board.
    """
    def backtrack(board, col):
        if col == n:
            solutions.append([[i, board[i]] for i in range(n)])
            return
        for row in range(n):
            board[col] = row
            if is_safe(board, col):
                backtrack(board, col + 1)

    solutions = []
    board = [-1] * n
    backtrack(board, 0)
    return solutions


def main():
    """Main function to run the N Queens solver."""
    n = validate_input(sys.argv)
    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
