"""
Print the following pattern for N number as input
0
1 2
2 3 4
3 4 5 6
4 5 6 7 8
5 6 7 8 9 10
"""

for i in range(6): # 0, 1, 2, 3, 4, 5
    for j in range(i+1):
        # i --> i + 1 ~~ Pattern matching comparison
        # 0 --> 0 ~~ 0
        # 1 --> 0, 1 ~~ 1, 2 --> +1
        # 2 --> 0, 1, 2 ~~ 2, 3, 4 --> +2
        # 3 --> 0, 1, 2, 3 ~~ 3, 4, 5, 6 --> +3
        print(j+i, end=" ")
    print()
    