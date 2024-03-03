for _ in range(int(input())):
    n, m = map(int, input().split())
    guns = sorted(map(int,input().split()))
    rate, cnt = 0, 0
    for r in guns:
        rate += r
        if rate <= m:
            cnt += 1
        else:
            break
    print(cnt)