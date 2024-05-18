for _ in range(int(input())):
    s = input()
    a, b, c, d = int(s[0]), int(s[1]), int(s[2]), int(s[3])
    and1 = a & b
    not1 = ~c & 1
    or1 = and1 | not1
    and2 = or1 & d
    not2 = ~and2 & 1
    print(bool(not2))
    