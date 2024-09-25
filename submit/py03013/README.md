## py03013
The formula used in the function `f(x, n)` is based on the concept of counting digit occurrences in a range by examining each digit place (units, tens, hundreds, etc.). Let's break down the logic behind the formula and understand why it works.

### Concept

To count how many times a digit `x` appears in all numbers from 0 to `n`, we need to consider each digit place separately. For example, if we are counting the digit `1` in the range from 0 to 456, we need to consider the units place, tens place, hundreds place, etc.

### Detailed Explanation

#### Variables:
- `m = 10**i`: Represents the current digit place (1, 10, 100, etc.).
- `a = n // m`: Represents the number of complete sets of `m` in `n`.
- `b = n % m`: Represents the remainder when `n` is divided by `m`.
- `z = a % 10`: Represents the digit at the current place.

#### Counting Logic:

1. **Complete Sets of `m`**:
   - `a // 10` gives the number of complete sets of `m` without considering the current digit place.
   - For example, if `n = 456` and `m = 10`, then `a = 456 // 10 = 45` and `b = 456 % 10 = 6`. Here, `a // 10 = 4` gives the number of complete sets of 10.

2. **Current Digit Place**:
   - `z = a % 10` gives the digit at the current place.
   - For example, if `a = 45`, then `z = 45 % 10 = 5`.

3. **Counting Occurrences**:
   - **If `z > x`**: The digit `x` appears in all the complete sets of `m` plus one more set.
     ```python
     ret += ((a // 10) + 1) * m
     ```
     - This accounts for the extra set where the digit at the current place is greater than `x`.
   - **If `z == x`**: The digit `x` appears in all the complete sets of `m` plus the remainder `b + 1`.
     ```python
     ret += (a // 10) * m + (b + 1)
     ```
     - This accounts for the exact number of times `x` appears at the current place, including the remainder part.
   - **If `z < x`**: The digit `x` appears in all the complete sets of `m`.
     ```python
     ret += (a // 10) * m
     ```
     - This accounts for the cases where the digit at the current place is less than `x`.

4. **Special Case for `x == 0`**:
   - When counting zeros, we need to adjust for leading zeros which are not counted.
     ```python
     if x == 0: ret -= m
     ```
   - This adjustment ensures that leading zeros are not included in the count.

### Example Walkthrough

Let's go through an example to see how the formula works in practice.

#### Example: Counting digit `1` in the range 0 to 456

1. **Units Place (`m = 1`)**:
   - `a = 456 // 1 = 456`
   - `b = 456 % 1 = 0`
   - `z = 456 % 10 = 6`
   - Since `z > 1`, we add `((456 // 10) + 1) * 1 = 46 * 1 = 46` to the count.

2. **Tens Place (`m = 10`)**:
   - `a = 456 // 10 = 45`
   - `b = 456 % 10 = 6`
   - `z = 45 % 10 = 5`
   - Since `z > 1`, we add `((45 // 10) + 1) * 10 = 5 * 10 = 50` to the count.

3. **Hundreds Place (`m = 100`)**:
   - `a = 456 // 100 = 4`
   - `b = 456 % 100 = 56`
   - `z = 4 % 10 = 4`
   - Since `z < 1`, we add `(4 // 10) * 100 = 0 * 100 = 0` to the count.

4. **Total Count**:
   - The total count of digit `1` in the range 0 to 456 is `46 + 50 + 0 = 96`.

### Summary

The formula used in the function `f(x, n)` leverages the positional properties of digits to count occurrences efficiently. By breaking down the problem into smaller subproblems based on each digit place, the function can handle large ranges without iterating through every number. This approach ensures that the solution is both efficient and scalable.
- [py03013.py](py03013.py)
- [input.txt](input.txt)
- [output.txt](output.txt)
