
# Python program to illustrate the given problem 
def calculate(n, power): 
    return sum([int(i) for i in str(pow(n, power))]) 
      
# Driver Code 
n = 5
power = 4
print (calculate(n, power)) 
