def hamming_distance(num1, num2):
    # XOR the two numbers to get the bits that differ
    xor_result = num1 ^ num2
    
    # Count the number of set bits in the XOR result
    # This is the Hamming distance
    hamming_dist = 0
    while xor_result:
        hamming_dist += xor_result & 1
        xor_result >>= 1
    
    return hamming_dist

# Input
t = int(input("Enter the number of test cases: "))
for _ in range(t):
    num1, num2 = map(int, input().split())
    
    # Output
    print(hamming_distance(num1, num2))
