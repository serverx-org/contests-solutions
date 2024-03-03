# Get The String

**Problem Statement:**

Given a string, Str, you can replace a character with its next character in the alphabet. You need to find a string such that it will become the first in dictionary order after performing K such operations.

**Input format:**

- The first line contains an integer, T, denoting the number of test cases.
- For each test case:
  - The first line contains two space-separated integers, N and K, denoting the length of string Str and the number of operations to be performed, respectively.
  - The second line contains string Str consisting of lowercase letters.

**Output Format:**

Print a string such that it will become the first in dictionary order after performing K such operations.

**Constraints:**

- 1 ≤ T ≤ 100
- 1 ≤ N ≤ 10^5
- 0 ≤ K ≤ 10^5

**Sample Input:**
```
2
1 3
x
3 3
zya
```

**Sample Output:**
```
a
aaa
```