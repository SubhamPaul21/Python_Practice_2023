"""Q2.Print the following pattern for the given number of rows.
Note: N is always odd.

Input format :
N (Total no. of rows and can only be odd)

Output format :
Pattern in N lines

Sample Input 1:
5
Sample Output 1:
 *
 ***
*****
 ***
  *

Constraints :
1 <= N <= 49
"""

import math

def diamond_star_pattern(n):
    if 1 <= n <= 49 and n % 2 != 0:
        mid = math.ceil(n / 2)

        # Forward pattern loop
        for i in range(mid):
            # spacing loop
            for j in range(mid - i - 1): print(" ", end=" ")
            # star loop
            for k in range(i+1, (i+1)*2): print("*", end=" ")
            # trailing star loop
            for l in range(i*2, i, -1): print("*", end=" ")
            print()

        # Reverse pattern loop
        for j in range(mid - 1, 0, -1):
            # spacing loop
            for m in range(mid - j): print(" ", end=" ")
            # star loop
            for n in range(j, j*2): print("*", end=" ")
            # trailing star loop
            for o in range(j, 1, -1): print("*", end=" ")
            print()
    else: print("Out of bound!")

diamond_star_pattern(21)