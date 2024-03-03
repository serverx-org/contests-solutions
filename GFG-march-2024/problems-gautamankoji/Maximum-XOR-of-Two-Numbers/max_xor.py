for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    res = 0
    for a in range(n):
        for b in range(a, n):
            if min(l[a], l[b]) >= abs(l[a] - l[b]):
                res = max(l[a] ^ l[b], res)
    print(res) 