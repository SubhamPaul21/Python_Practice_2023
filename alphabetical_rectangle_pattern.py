"""
Print the following pattern for the given N number of rows.
* Pattern for N = 3
A
BB
CCC

* Sample Input 1:7

Sample Output 1:
A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG

Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines

* Constraints
0 <= N <= 26
"""
# A --> 65
# Z --> 90

def alphabetic_pattern(n):
    if 0 <= n <= 26:
        # ascii_code_A = 65
        for i in range(n): # row range
            for j in range(i+1): # column range 
                print(chr(65 + i), end="")
            # ascii_code_A += 1
            print()
    else:
        print("Out of bound")

alphabetic_pattern(3)
print()
alphabetic_pattern(7)
print()
alphabetic_pattern(27)