import sys

# Parsing all the input data 
def parse_testcases(io):
    # Read the number of test cases
    T = int(io.readline())
    tc = []

    # For each test case
    for _ in range(T):
        # Read the input data
        (a, b) = map(int, io.readline().strip().split())
        # Add to the list fo test cases
        tc.append((a,b))

    # Return all the test cases parsed
    return tc

# Function to solve a single test case
def solve_testcase(t):
    # Get data from the test case
    # (a, b) = t

    # Evaluate the solution
   
   solutions = []

    for case in t:
        nums_to_check = []

        num = case.min()
        for i in range(num):
            if num % i == 0:
                nums_to_check.append(i)
        
        for i in nums_to_check:
            for nums in case:
                if nums % i == 0:
                    continue
                else:
                    nums_to_check.remove(i)

        tmp_solution = len(nums_to_check)
        solutions.append(tmp_solution)

    # Returning the solution
    return solution

# Solve 
def solve(input, output):
    # Enumerate all the test cases
    for i, t in enumerate(parse_testcases(input)):
        # Print the solution of the test case
        print(f"Case #{i+1}:", solve_testcase(t), file=output)

if __name__ == "__main__":
    fin = sys.stdin
    fout = sys.stdout
    # If you want to read and write from files use these two lines:
    
    fin = open("input.txt", "r")

    fout = open("output.txt", "w")

    solve(fin, fout)