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
        
        
def pattern_j(n):
    for i in range(1,n*2):
        stars =  i if i<= n else (n*2)-i
        for j in range(1,stars+1):
            print("*",end=" ")
        print("")

def pattern_k(n):
    for i in range(1,n+1):
        stars = i
        spaces = n-i
                
        for _ in range(1,spaces+1):
            print(" ",end="")
            
        for j in range(1,stars+1):
            print("*",end="")
        print("")
        
def pattern_l(n):
    for i in range(1,n+1):
        stars = (n-i)+1
        spaces = i-1
                
        for _ in range(1,spaces+1):
            print(" ",end="")
            
        for j in range(1,stars+1):
            print("*",end="")
        print("")

def pattern_m(n):
    for i in range(1,n+1):
        stars = (i*2)-1
        spaces = n-i
        
        for _ in range(1,spaces+1):
            print(" ",end="")
            
        for j in range(1,stars+1):
            print("*",end="")
        print("")

def pattern_n(n):
    for i in range(1,n+1):
        spaces = i-1
        stars = 2*(n-i)+1
        
        for _ in range(1,spaces+1):
            print(" ",end="")
            
        for j in range(1,stars+1):
            print("*",end="")
            
        print("")

def pattern_o(n):
    for i in range(1,(n*2-1)+1):
        effective_i = i if i<=n else n*2 - i

        stars = effective_i*2-1
        spaces = n-effective_i

        for _ in range(1,spaces+1):
            print(" ",end="")
            
        for j in range(1,stars+1):
            print("*",end="")
        
        print("")

def pattern_p(n):
    for i in range(1,(n*2)+1):
        effective_i = i if i<=n else n*2 - i + 1
        
        spaces = effective_i - 1
        stars = n-(effective_i-1)

        for _ in range(1,spaces+1):
            print(" ",end="")
            
        for j in range(1,stars+1):
            print("*",end=" ")
        
        print("")

def pattern_q(n):
    for i in range(1,n+1):
        space = n - i
        stars = i*2 -1 

        for _ in range(1,space+1):
            print(" ",end="")
        
        for j in range(1,stars+1):
            if j==1 or stars == j or i==n:
                print("*",end="")
            else:
                print(" ",end="")
        print("")

def pattern_r(n):
    for i in range(1,n+1):
        space = i-1
        stars = (n-i)*2 + 1

        for _ in range(1,space+1):
            print(" ",end="")
        
        for j in range(1,stars+1):
            if j==1 or stars == j or i==1:
                print("*",end="")
            else:
                print(" ",end="")
        print("")

def pattern_s(n):
    for i in range(1,n*2):
        core_i = i if i <= n else (n*2)-i

        spaces = n-core_i
        stars = core_i*2 - 1

        for _ in range(1,spaces+1):
            print(" ",end="")
            
        for j in range(1,stars+1):
            if j==1 or j==stars:
                print("*",end="")
            else:
                print(" ",end="")
        
        print("")

def pattern_t(n):
    for i in range(1,n+1):
        for j in range(1,n):
            if j==1 or j==n-1 or i==1 or i==n:
                print("*",end="")
            else:
                print(" ",end="")
        
        print("")

def pattern_u(n):
    pass # Skipped for now 

def pattern_v(n):
    for i in range(1,(n*2)+1):
        effective_i = i if i <= n else n*2 - i + 1
        stars = n-effective_i+1
        spaces = effective_i*2 - 2
        
        # print("Stars :",stars)
        # print("Spaces :",spaces)
        
        for j in range(1,stars+1):
            print("*",end="")
        
        for _ in range(1,spaces+1):
            print("-",end="")
            
        for j in range(1,stars+1):
            print("*",end="")
            
        print("")

def pattern_v_optimized(n):
        for i in range(1,(n*2)+1):
            effective_i = i if i <= n else n*2 - i + 1
            stars = n-effective_i+1
            spaces = effective_i*2 - 2
            
            left_star_end = stars
            right_star_start = stars + spaces+1
            
            
            for j in range(1,(n*2)+1):

                if j <= left_star_end or right_star_start<=j:
                    print("*",end="")
                else:
                    print("-",end="")
                    
            print("")
            
def pattern_w(n):
    for i in range(1,n*2):
        effective_i =  i if i <= n else n*2-i
        stars = effective_i
        spaces = (n*2) - (effective_i*2)
        
        left_star_end = stars
        right_star_start = stars + spaces+1
        
        
        for j in range(1,(n*2)+1):

            if j <= left_star_end or right_star_start<=j:
                print("*",end="")
            else:
                print(" ",end="")
                
        print("")
            

def pattern_x(n):
    pass

def pattern_y(n):
    pass

def pattern_z(n):
    pass

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
    # pattern_j(5)
    # pattern_k(5)
    # pattern_l(5)
    # pattern_m(5)
    # pattern_n(5)
    # pattern_o(5)
    # pattern_p(5)
    # pattern_q(5)
    # pattern_r(5)
    # pattern_s(5)
    # pattern_t(5)
    # pattern_u(5)
    # pattern_v(5)
    # pattern_v_optimized(5)
    pattern_w(5)