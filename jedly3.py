
def calculate(n, power): 
    return sum([int(i) for i in str(pow(n, power))])      
n = 5
power = 4
print (calculate(n, power)) 
