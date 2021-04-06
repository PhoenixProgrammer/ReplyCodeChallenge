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
        (N, k) = map(int, io.readline(  ).strip().split())
        # Read the input data
        inputAntennas = list(map(int, io.readline(  ).strip().split()))
        inputBuildings = list(map(int, io.readline(  ).strip().split()))
        # Add to the list fo test cases
        tc.append([k, inputAntennas, inputBuildings])

    # Return all the test cases parsed
    print(tc)
    return tc

# Function to solve a single test case
def solve_testcase(t):
    k = t[0]

    A = t[1]
    B = t[2]
    temp_min = 0
    for _ in range(k):
        if (min(A) >= 0 and min(B) >= 0):
            temp_min += min(A) * min(B)
            A.remove(min(A))
            B.remove(min(B))
        else:
            pass

    A = t[1]
    B = t[2]
    temp_max = 0
    for _ in range(k):
        if (min(A) * min(B)) > (max(A) * max(A)):
            temp_max += min(A) * min(B)
            A.remove(min(A))
            B.remove(min(B))
        else:
            temp_max += max(A) * max(B)
            A.remove(max(A))
            B.remove(max(B))

    return str(f"{temp_min} {temp_max}")

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
    fin = open(join(current_dir, "./input-antennas-26b7.txt"), "r")
    fout = open(join(current_dir, "./output.txt"), "w")
    solve(fin, fout)
