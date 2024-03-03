**Problem Statement:  THE NAME IS BOND, JAMES BOND**

Agent 007 is on a new mission, planning an ambush attack at the villain's base. He has N weapons available, each with its attack rating. However, there's a limitation: the total attack rating of weapons he carries must not exceed K. Agent 007 aims to maximize the number of weapons he can take while abiding by this restriction. Your task is to determine the maximum number of weapons Agent 007 can carry for his mission.

**Input:**

- The first line contains an integer, T, denoting the number of test cases.
- For each test case:
  - The first line contains two space-separated integers, N and K, where N is the number of weapons and K is the limitation value set by the intelligence service.
  - The second line contains N space-separated integers denoting the attack rating of each weapon.

**Output:**

For each test case, print the maximum number of weapons Agent 007 can take with him for the mission.

**Constraints:**

- 1 <= T <= 10
- 1 <= N <= 10^5
- 1 <= K <= 10^9
- 1 <= weapon_attack_rating <= 10^9

**Sample Input:**
```
1
4 3
4 5 2 1
```

**Sample Output:**
```
2
```