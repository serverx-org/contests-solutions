def max_value_no_consecutive_bits(n):
    # Convert n to binary string
    binary_str = bin(n)[2:]
    
    # Convert binary string to list of integers
    bits = list(map(int, binary_str))
    
    # Iterate through bits to make sure no three consecutive bits are set
    for i in range(2, len(bits)):
        if bits[i] == 1 and bits[i-1] == 1 and bits[i-2] == 1:
            bits[i] = 0  # Change the third consecutive bit to 0
    
    # Convert modified list of bits back to integer
    new_value = int(''.join(map(str, bits)), 2)
    
    return new_value

# Test cases
test_cases = int(input("Enter the number of test cases: "))
for _ in range(test_cases):
    n = int(input())
    print(max_value_no_consecutive_bits(n))
