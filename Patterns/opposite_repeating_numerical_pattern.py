"""
Print the following pattern for the given N number of rows.
Input format :
Integer N (Total no. of rows)

Output format :
Pattern in N lines

Pattern for N = 4
4444
333
22
1

Sample Input 1:
5
Sample Output 1:
55555 
4444
333
22
1

Constraints :
0 <= N <= 50

"""

def opposite_repeating_numerical_pattern(n):
    if 0 <= n <= 50:
        temp_n = n
        for i in range(n):
            for j in range(n):
                if (i + j <= n - 1):
                    print(temp_n, end=" ")
                else:
                    print(" ", end=" ")
            temp_n -= 1
            print()
    else:
        print("Out of bound!")

opposite_repeating_numerical_pattern(10)