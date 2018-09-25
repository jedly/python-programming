2
3
4
5
6
7
8
9
10
11
12
13
	
num = int(input("enter a number: "))
 
temp = num
rev = 0
 
while temp != 0:
    rev = (rev * 10) + (temp % 10)
    temp = temp // 10
 
if num == rev:
    print("number is palindrome")
else:
    print("number is not palindrome")
