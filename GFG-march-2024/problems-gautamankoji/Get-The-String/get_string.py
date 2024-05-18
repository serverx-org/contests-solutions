for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input().strip())
    i = 0
    while k > 0 and i < n:
        if s[i] != 'a':
            s[i] = chr((ord(s[i]) - 96) % 26 + 97)
            k -= 1
        else:
            i += 1
    print(''.join(s))
