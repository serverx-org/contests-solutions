## Problem Statement: Cricket Analyst of the year

As a cricket analyst for a prestigious team preparing for the upcoming IPL season, you aim to impress team owners by presenting the analysis of a player's performance. You possess a series of scores for the player, and you seek to identify the longest strictly increasing sequence of these scores to showcase the player's consistency and potential. The sequence need not comprise consecutive match scores but must exhibit a strictly ascending trend. Your task is to determine the length of this longest increasing sequence for each test case.

### Input

- The first line contains an integer, T, denoting the number of test cases.
- For each test case:
  - The first line contains an integer, N, representing the number of scores for the player.
  - The second line contains N space-separated integers representing the scores.

### Output

For each test case, output the length of the longest strictly increasing sequence of scores.

### Constraints

- 1 < T < 10
- 1 < N < 10^3
- 1 < scores < 300

### Example

Input:
```
1
3
2 1 5
```

Output:
```
2
```
