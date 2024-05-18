**Problem Statement: World of Narnia**

In the world of Narnia, Lucy Pevensie enters through her Wardrobe with a Watch that shows only time and date. Lucy recalls entering the Wardrobe on New Year's Day on Earth. She is confident that she is still in the same year but wants to determine how many days she has spent in the world of Narnia. The watch displays the Date (D), Month (M), and Year (Y). Help Lucy calculate the number of days she has been away from Earth.

**Input:**

The input consists of several test cases. Each test case is described on a single line containing three integers: D, M, and Y, representing the date, month, and year, respectively.

**Output:**

For each test case, output the number of days Lucy has been away from Earth, including the 1st of January and the given date.

**Constraints:**

- 1 <= D <= 31
- 1 <= M <= 12
- 1900 <= Y <= 24000

**Example:**

Input:
```
6
15 6 1959
19 9 2071
2 3 1956
6 3 2018
27 2 2106
23 10 2117
```

Output:
```
166
262
62
65
58
296
```