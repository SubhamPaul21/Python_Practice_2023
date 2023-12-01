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
# First Approach
def opposite_numerical_pattern_approach1(n):
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


opposite_numerical_pattern_approach1(10)


# Second Approach
def opposite_numerical_pattern_approach2(n):
    if 0 <= n <= 50:
        # row loop
        for i in range(n): 
            # spacing loop where for each row i we have (n-i-1) space
            for j in range(n-i-1): 
                print(" ", end=" ")
            # number printing loop based on i
            for k in range(1, i+2): 
                print(k, end=" ")
            print()
    else:
        print("Out of bound!")


opposite_numerical_pattern_approach2(10)