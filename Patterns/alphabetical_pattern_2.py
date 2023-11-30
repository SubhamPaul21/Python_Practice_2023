"""Print the following pattern for the given N number of rows.

Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines

Pattern for N = 4
A
B C
C D E
D E F G

Pattern for N = 6
A
B C
C D E
D E F G
E F G H I
F G H I J K


Constraints
0 <= N <= 13

"""

def alphabetical_pattern(n):
    if 0 <= n <= 13:
        for i in range(n):
            for j in range(i+1):
                print(chr(65 + (j+i)), end=" ")
            print()
    else:
        print("Out of bound!")

alphabetical_pattern(4)
print()
alphabetical_pattern(6)