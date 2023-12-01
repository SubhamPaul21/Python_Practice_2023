"""
Q1. Print the following pattern for the given number of rows.
Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines

Sample Input 1:
5
Sample Output 1:
          1
          232
         34543
        4567654
       567898765

Constraints :
0 <= N <= 50
"""


def pyramid_numerical_pattern(n):
    if 0 <= n <= 50:
        # row loop
        for i in range(n):
            # spacing loop
            for j in range(n-i-1):
                print(" ", end=" ")
            # front till middle -- number printing loop
            for k in range(i+1, (i+1)*2):
                print(k, end=" ")
            # reverse number printing loop
            for l in range(i*2, i, -1):
                print(l, end=" ")
            print()
    else:
        print("Out of bound!")


pyramid_numerical_pattern(5)
