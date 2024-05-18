def find_duplicate_and_replace(N, arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            duplicate = num
        else:
            frequency[num] = True
    
    # Find a replacement roll number
    replacement = 1
    while replacement in frequency:
        replacement += 1
    
    return duplicate, replacement

# Input
N = int(input())
arr = list(map(int, input().split()))

# Find duplicate and replacement
duplicate, replacement = find_duplicate_and_replace(N, arr)

# Output
print(duplicate, replacement)
