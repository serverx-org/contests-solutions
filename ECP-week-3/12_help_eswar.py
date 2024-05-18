import math

def min_operations(N):
    count = 0
    while N > 0:
        max_power_of_2 = int(math.log2(N))
        N -= 2**max_power_of_2
        count += 1
    return count

# Input
T = int(input("Enter number of test cases: "))
test_cases = []
for _ in range(T):
    test_cases.append(int(input()))

# Output
for N in test_cases:
    print(min_operations(N))
