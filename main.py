def pattern_a(n):
    for row in range(1,n+1):
        for col in range(1,n+1):
            print("*",end=" ")
        print("")
        
def pattern_b(n):
    for row in range(1,n+1):
        for col in range(1,n+1):
            print(row,end=" ")
        print("")

def pattern_c(n):
    for row in range(1,n+1):
        for col in range(1,row+1):
            print("*",end=" ")
        print("")

def pattern_d(n):
    for row in range(1,n+1):
        for col in range(1,row+1):
            print(col,end=" ")
        print("")

def pattern_e(n):
    for row in range(1,n+1):
        val = 0 if row%2 == 0 else 1
        for col in range(1,row+1):
            print(val,end=" ")
            val = int(not val) # 1-val
        print("")

def pattern_f(n):
    val = 1
    for row in range(1,n+1):
        for col in range(1,row+1):
            print(val,end=" ")
            val+=1
        print("")

def pattern_g(n):
    for row in range(1,n+1):
        for col in range(1,(n-(row-1))+1): # +1 for for loop
            print("*",end=" ")
        print("")
# 5-0 Calculate the 0 is matter now
# 5-1 so we can try to relate row and col to find it
# 5-2

def pattern_h(n):
    for row in range(1,n+1):
        col = n-(row-1)
        for j in range(1,col+1): # +1 for for loop
            print(col,end=" ")
        print("")

def pattern_i(n):
    for row in range(1,n+1):
        col = n-(row-1)
        for j in range(1,col+1): # +1 for for loop
            print(j,end=" ")
        print("")
        
        
def pattern_j(n):
    for row in range(1,n*2):
        stars =  row if row<= n else (n*2)-row
        for col in range(1,stars+1):
            print("*",end=" ")
        print("")

def pattern_k(n):
    for row in range(1,n+1):
        stars = row
        spaces = n-row

        for _ in range(1,spaces+1):
            print(" ",end="")

        for col in range(1,stars+1):
            print("*",end="")
        print("")
        
def pattern_l(n):
    for row in range(1,n+1):
        stars = (n-row)+1
        spaces = row-1

        for _ in range(1,spaces+1):
            print(" ",end="")

        for col in range(1,stars+1):
            print("*",end="")
        print("")

def pattern_m(n):
    for row in range(1,n+1):
        stars = (row*2)-1
        spaces = n-row

        for _ in range(1,spaces+1):
            print(" ",end="")

        for col in range(1,stars+1):
            print("*",end="")
        print("")

def pattern_n(n):
    for row in range(1,n+1):
        spaces = row-1
        stars = 2*(n-row)+1

        for _ in range(1,spaces+1):
            print(" ",end="")

        for col in range(1,stars+1):
            print("*",end="")

        print("")

def pattern_o(n):
    for row in range(1,(n*2-1)+1):
        effective_row = row if row<=n else n*2 - row

        stars = effective_row*2-1
        spaces = n-effective_row

        for _ in range(1,spaces+1):
            print(" ",end="")

        for col in range(1,stars+1):
            print("*",end="")

        print("")

def pattern_p(n):
    for row in range(1,(n*2)+1):
        effective_row = row if row<=n else n*2 - row + 1

        spaces = effective_row - 1
        stars = n-(effective_row-1)

        for _ in range(1,spaces+1):
            print(" ",end="")

        for col in range(1,stars+1):
            print("*",end=" ")

        print("")

def pattern_q(n):
    for row in range(1,n+1):
        space = n - row
        stars = row*2 -1

        for _ in range(1,space+1):
            print(" ",end="")

        for col in range(1,stars+1):
            if col==1 or stars == col or row==n:
                print("*",end="")
            else:
                print(" ",end="")
        print("")

def pattern_r(n):
    for row in range(1,n+1):
        space = row-1
        stars = (n-row)*2 + 1

        for _ in range(1,space+1):
            print(" ",end="")

        for col in range(1,stars+1):
            if col==1 or stars == col or row==1:
                print("*",end="")
            else:
                print(" ",end="")
        print("")

def pattern_s(n):
    for row in range(1,n*2):
        core_row = row if row <= n else (n*2)-row

        spaces = n-core_row
        stars = core_row*2 - 1

        for _ in range(1,spaces+1):
            print(" ",end="")

        for col in range(1,stars+1):
            if col==1 or col==stars:
                print("*",end="")
            else:
                print(" ",end="")

        print("")

def pattern_t(n):
    for row in range(1,n+1):
        for col in range(1,n):
            if col==1 or col==n-1 or row==1 or row==n:
                print("*",end="")
            else:
                print(" ",end="")

        print("")

def pattern_u(n):
    pass # Skipped for now 

def pattern_v(n):
    for row in range(1,(n*2)+1):
        effective_row = row if row <= n else n*2 - row + 1
        stars = n-effective_row+1
        spaces = effective_row*2 - 2

        # print("Stars :",stars)
        # print("Spaces :",spaces)

        for col in range(1,stars+1):
            print("*",end="")

        for _ in range(1,spaces+1):
            print("-",end="")

        for col in range(1,stars+1):
            print("*",end="")

        print("")

def pattern_v_optimized(n):
        for row in range(1,(n*2)+1):
            effective_row = row if row <= n else n*2 - row + 1
            stars = n-effective_row+1
            spaces = effective_row*2 - 2

            left_star_end = stars
            right_star_start = stars + spaces+1


            for col in range(1,(n*2)+1):

                if col <= left_star_end or right_star_start<=col:
                    print("*",end="")
                else:
                    print("-",end="")

            print("")
            
def pattern_w(n):
    for row in range(1,n*2):
        effective_row =  row if row <= n else n*2-row
        stars = effective_row
        spaces = (n*2) - (effective_row*2)

        left_star_end = stars
        right_star_start = stars + spaces+1


        for col in range(1,(n*2)+1):

            if col <= left_star_end or right_star_start<=col:
                print("*",end="")
            else:
                print(" ",end="")

        print("")
            

def pattern_x(n):
    for row in range(1,n+1):
        spaces = n-row
        numbers = row*2 - 1
        for col in range(1,spaces+1):
            print(" ",end="")
        for col in range(row,0,-1):
            print(col,end="")
        for col in range(2,row+1):
            print(col,end="")
        print("")

def pattern_x_optimized(n):
    pass
        

def pattern_y(n):
    for row in range(1,n+1):
        spaces = (n*2) - (row*2)
        for col in range(1,row+1):
            print(col,end="")
        for col in range(1,spaces+1):
            print(" ",end="")
        for col in range(row,0,-1):
            print(col,end="")
        print("")
        

def pattern_z(n):
    for row in range(1,n*2):
        for col in range(1,n*2):
            left = col
            right = n*2 - col 
            top = row 
            down = n*2 - row
            value = n- min(left,right,top,down)+1
            print(value,end="")
        print()

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
    # pattern_w(5)
    # pattern_x(5)
    # pattern_y(5)
    pattern_z(7)