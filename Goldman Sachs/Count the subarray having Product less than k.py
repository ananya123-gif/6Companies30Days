#Solution in Python 

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        c=0
        prod = 1
        i=0
        j=0
        
        while(j<n):
            prod=prod*a[j]
            if(prod>=k):
                while(prod>=k and i<=j):
                    prod/=a[i]
                    i=i+1
        
            c=c+(j-i+1)
            j=j+1
            
        return c
