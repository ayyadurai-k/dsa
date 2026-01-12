def pattern_a(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print("*",end=" ")
        print("")
        
def pattern_b(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i,end=" ")
        print("")

def pattern_c(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print("")

def pattern_d(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print("")

def pattern_e(n):
    for i in range(1,n+1):
        val = 0 if i%2 == 0 else 1
        for j in range(1,i+1):
            print(val,end=" ")
            val = int(not val) # 1-val
        print("")

def pattern_f(n):
    val = 1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(val,end=" ")
            val+=1
        print("")

def pattern_g(n):
    for i in range(1,n+1):
        for j in range(1,(n-(i-1))+1): # +1 for for loop 
            print("*",end=" ")
        print("")
# 5-0 Calculate the 0 is matter now
# 5-1 so we can try to relate row and col to find it
# 5-2

def pattern_h(n):
    for i in range(1,n+1):
        col = n-(i-1)
        for j in range(1,col+1): # +1 for for loop 
            print(col,end=" ")
        print("")

def pattern_i(n):
    for i in range(1,n+1):
        col = n-(i-1)
        for j in range(1,col+1): # +1 for for loop 
            print(j,end=" ")
        print("")
        

def pattern_i(n):
    for i in range(1,n+1):
        col = n-(i-1)
        for j in range(1,col+1): # +1 for for loop 
            print(j,end=" ")
        print("")
        
def pattern_j(n):
    sub=2
    for i in range(1,n*2):
        stars =  i if i<= n else (n*2)-i

        for j in range(1,stars+1):
            print("*",end=" ")
        print("")

if __name__ == "__main__":
    # pattern_a(5)
    # pattern_b(5)
    # pattern_c(5)
    # pattern_d(5)
    # pattern_e(5)
    # pattern_e(5)
    # pattern_f(5)
    # pattern_g(5)
    # pattern_h(5)
    # pattern_i(5)
    pattern_j(5)
    