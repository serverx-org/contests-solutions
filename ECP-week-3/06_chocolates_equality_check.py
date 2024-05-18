def can_distribute_equally(n, m):
    total_chocolates = n + m
    # If the total number of chocolates is odd, it's impossible to distribute equally
    if total_chocolates % 2 != 0:
        return False
    # If both have the same number of chocolates, return True
    if n == m:
        return True
    # Otherwise, it's only possible if the total number of chocolates is divisible by 2
    return total_chocolates % 2 == 0

# Read the number of test cases
T = int(input("Enter the number of test cases: "))
results = []

# Iterate over each test case
for _ in range(T):
    n, m = map(int, input().split())
    results.append(can_distribute_equally(n, m))

# Print the results
for result in results:
    print("True" if result else "False")
