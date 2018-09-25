

  
def Nth_of_AP(a, d, N) : 
  
    Nth term t(n) = a(1) + (n-1)*d 
    return (a + (N - 1) * d) 
       
   

a = 2  # starting number 
d = 1  # Common difference 
N = 5  # N th term to be find 
   

print( "The ", N ,"th term of the series is : ", 
       Nth_of_AP(a, d, N)) 
  
  
  
