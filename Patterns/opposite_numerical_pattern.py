"""Print the following pattern for the given N number of rows.
Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines

The dots represent spaces.

Sample Input 2:
4

Sample Output 2:
   1 
  12
 123
1234

Constraints
0 <= N <= 50
"""

def opposite_numerical_pattern(n):
    if 0 <= n <= 50:
        for i in range(n):
            temp_n = 1
            for j in range(n):
                if (i + j < n - 1):
                    print(" ", end=" ")
                else:
                    print(temp_n, end=" ")
                    temp_n += 1
            print()
    else:
        print("Out of bound!")


opposite_numerical_pattern(10)