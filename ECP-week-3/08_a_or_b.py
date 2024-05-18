def min_flips_to_or(a, b, c):
    flips = 0
    for i in range(31, -1, -1):  # Considering 32-bit integers
        bit_a = (a >> i) & 1
        bit_b = (b >> i) & 1
        bit_c = (c >> i) & 1
        
        if (bit_a | bit_b) != bit_c:
            if bit_c == 1:  # If bit_c is 1, we need to flip a or b to make it 1
                if bit_a == 0 and bit_b == 0:  # If both a and b are 0, flip any one
                    flips += 1
                elif bit_a == 1 and bit_b == 1:  # If both a and b are 1, flip any one
                    flips += 1
            else:  # If bit_c is 0, we need to ensure both a and b are 0
                flips += (bit_a + bit_b)
                
    return flips

# Input
t = int(input("Enter the number of test cases: "))
for _ in range(t):
    a, b, c = map(int, input().split())
    print(min_flips_to_or(a, b, c))
