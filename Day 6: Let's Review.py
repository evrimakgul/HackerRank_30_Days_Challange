# Enter your code here. Read input from STDIN. Print output to STDOUT
for n in range(int(input())):
    s = str(input())
    s1 = str()
    s2 = str()
    for i,j in enumerate(s):
        if i % 2 == 0:
            s1 += j
        else:
            s2 += j
    print(s1, s2)
