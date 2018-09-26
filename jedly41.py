

def isPowerOfTwo(n): 
    if (n == 0): 
        return False
    while (n != 1): 
            if (n % 2 != 0): 
                return False
            n = n // 2
              
    return True
  

if(isPowerOfTwo(31)): 
    print('Yes') 
else: 
    print('No') 
if(isPowerOfTwo(64)): 
    print('Yes') 
else: 
    print('No') 
  

