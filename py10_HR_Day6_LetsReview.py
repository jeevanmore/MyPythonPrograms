##Day 6: Let's Review
##The first line contains an integer, t (the number of test cases).
##Each line n of the t subsequent lines contain a String, s.
##Sample Input
##
##2
##Hacker
##Rank
##Sample Output
##
##Hce akr
##Rn ak
##

# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for n in range(t):
    s = input()
    print (s[::2], s[1::2])

##Alternate Solution: for i in range(int(input())): s=input(); print(*["".join(s[::2]),"".join(s[1::2])])
