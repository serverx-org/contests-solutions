def binary_to_decimal(binary_string):
    decimal_value = int(binary_string, 2)
    return decimal_value

def flip_even_indices(binary_input):
    res = ''
    for i in range(len(binary_input)):
        if i % 2 != 0:
            if binary_input[i] == '0':
                res += '1'
            else:
                res += '0'
        else:
            res += binary_input[i]
    return res


n = int(input())
binary_input = bin(n)[2:]

flipped_binary_string = flip_even_indices(binary_input)
decimal_value = binary_to_decimal(flipped_binary_string)

print("Input Binary String:", binary_input)
print("Flipped Binary String:", flipped_binary_string)
print("Decimal Value:", decimal_value)
