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

def diamond_star_pattern(n):
  if 1 <= n <= 49:
    if n % 2 != 0:
      mid = (n // 2) + 1

      # first part row loop
      for i in range(mid):
        # space printing loop
        for j in range(mid - i - 1):
          print(".", end=" ")
        # star printing loop
        for j in range((2 * i) + 1):
          print("*", end=" ")
        # print new line
        print()

      # second part row loop
      for i in range(1, mid):
        # space printing loop
        for j in range(i):
          print(".", end=" ")
        # reverse star printing loop
        for j in range(n - (2 * i)):
          print("*", end=" ")
        # print new line
        print()
    else:
      print("Enter odd number only")
  else:
    print("Out of bound!")

diamond_star_pattern(5)