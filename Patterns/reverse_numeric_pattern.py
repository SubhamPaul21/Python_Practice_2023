"""
Print the following pattern -->
n = 5
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
0 1 2 3 4 5
"""

def reverse_numeric_pattern(n):
    for i in range(n+1):
        for j in range(i+1):
            print((n - i) + j, end=" ")
        print()

reverse_numeric_pattern(5)