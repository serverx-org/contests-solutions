# Stripe Sum Challenge

**Problem Statement:**

Ravi and Vinod, students from city S, boarded a train for the All-Berland Olympiad. In a carriage with \( n \) compartments, they aimed to avoid boredom by rearranging themselves so no compartment had one or two students. Seeking help from a conductor, they aimed to find the minimum number of swaps needed for a fun-filled journey with groups of three or four in each compartment.

**Input:**

- The first line contains a single integer, \( T \), denoting the number of test cases.
- For each test case:
  - The first line contains a single integer, \( N \), denoting the length of the array.
  - The second line contains \( N \) space-separated integers.

**Output:**

If no sequence of seat swapping achieves the desired result, output the number "-1". Otherwise, display the minimum number of individuals that need persuading to swap seats and reach the desired configuration.

**Constraints:**

- \( 1 \leq T \leq 10 \)
- \( 1 \leq N \leq 10^5 \)
- \( 1 \leq A_i \leq 10^5 \)

**Sample Input:**

```
3
8
0 2 3 2 4 1 4 1
5
3 3 3 2 2
10
1 4 1 3 3 1 1 3 1 2
```

**Sample Output:**

```
2
2
4
```
