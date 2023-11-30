"""Print the following pattern for the given number of rows.
Input format :
N (Total no. of rows)

Output format :
Pattern in N lines

Pattern for N = 5
E
D E
C D E
B C D E
A B C D E

Pattern for N = 8
H
G H
F G H
E F G H
D E F G H
C D E F G H
B C D E F G H
A B C D E F G H

Constraints
0 <= N <= 26
"""

def reverse_alphabetic_pattern(n):
    if 0 <= n <= 26:
        for i in range(n):
            for j in range(i+1):
                print(chr(64 + ((n - i) + j)), end=" ")
            print()
    else:
        print("Out of bound!")

reverse_alphabetic_pattern(5)
print()
reverse_alphabetic_pattern(8)