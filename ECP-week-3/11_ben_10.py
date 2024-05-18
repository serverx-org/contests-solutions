def min_operations(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + min_operations(n // 2)
    else:
        return 1 + min(min_operations(n + 1), min_operations(n - 1))

# Input
t = int(input("Enter number of test cases: "))
test_cases = []
for _ in range(t):
    test_cases.append(int(input()))

# Output
for n in test_cases:
    print(min_operations(n))


# gives tle if removed recursion then 100