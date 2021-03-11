#!/usr/bin/env python3
from os.path import dirname, join

# Parsing all the input data 
def parse_testcases(io):
    # Read the number of test cases
    T = int(io.readline())
    tc = []

    # For each test case
    for _ in range(T):
        (N, k) = map(int, io.readline().strip().split())
        input_two = list(map(int, io.readline().strip().split()))
        tc.append([(N, k), input_two])

    return tc

# Function to solve a single test case
def solve_testcase(t):
    (N, k) = t[0]
    permutation = t[1]

    positions = list(range(N))
    for _ in range(k):
        positions = [positions[i] for i in permutation]

    return ' '.join(map(str, positions))

# Solve 
def solve(input, output):
    # Enumerate all the test cases
    for i, t in enumerate(parse_testcases(input)):
        # Print the solution of the test case
        # print(f"Case #{i+1}:", solve_testcase(t), file=output)
        print(i)
        print(f"Case #{i+1}:", solve_testcase(t), file=output)

current_dir = dirname(__file__)

if __name__ == "__main__":
    fin = open(join(current_dir, "./input-seats-b574.txt"), "r")
    fout = open(join(current_dir, "./output.txt"), "w")
    solve(fin, fout)