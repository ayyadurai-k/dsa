""" 
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""

def print_a(n):
    for i in range(1,n*2):
        spaces = 0
        stars = 0
        
        if i <= n:
            spaces = n-i
            stars = (n*2-1)-(spaces*2)
            
        else :
            spaces = i-n
            stars = (n*2-1)-(spaces*2)
        
        for _ in range(1,spaces+1):
            print(" ",end="")
            
        for _ in range(1,stars+1):
            print("*",end="")
            
        print("")
        
        


if __name__ == "__main__":
    print_a(5)

