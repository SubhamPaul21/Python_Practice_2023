"""Question 1.
for n=3     
pattern is 
1
2 2
3 3 3

for n=5
pattern is 
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
now print for n=6!!
"""
for i in range(5):
    for j in range(i+1):
        print(i+1, end=" ")
    print()