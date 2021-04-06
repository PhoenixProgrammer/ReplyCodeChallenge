#!/usr/bin/env python3

import sys
from os.path import dirname, join
import math

# Parsing all the input data 
def parse_testcases(io):
    # Read the number of test cases
    T = int(io.readline())
    tc = []

    # For each test case
    for _ in range(T):
        # Read number of gadgets
        N = int(io.readline())
        # Read the input data
        input = list(map(int, io.readline(  ).strip().split()))
        # Add to the list fo test cases
        tc.append(list(input))

    # Return all the test cases parsed
    print(tc)
    return tc

# Function to solve a single test case
def solve_testcase(t):
    solution = 0

    nums_to_check = []
    num = min(t)

    for i in range(1, math.floor(num / 2) + 1):
        if num % i == 0:
            nums_to_check.append(i)
    nums_to_check.append(num)

    solutions = []
        
    for divisor in nums_to_check:
        c = True
        for num in t:
            if num % divisor == 0:
                continue
            else:
                c = False
        if c == True:
            solutions.append(divisor)
        
    solution = len(solutions)

    print(solution)
    return solution

# Solve 
def solve(input, output):
    # Enumerate all the test cases
    for i, t in enumerate(parse_testcases(input)):
        # Print the solution of the test case
        # print(f"Case #{i+1}:", solve_testcase(t), file=output)
        print(f"Case #{i+1}:", solve_testcase(t), file=output)

current_dir = dirname(__file__)

if __name__ == "__main__":
    # fin = sys.stdin
    # fout = sys.stdout
    # If you want to read and write from files use these two lines:
    fin = open(join(current_dir, "./input/input-kits-9ccf.txt"), "r")
    fout = open(join(current_dir, "./output.txt"), "w")
    solve(fin, fout)
