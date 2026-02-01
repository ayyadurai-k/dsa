

def pattern_17(n):
    for row in range(1,n*2):
        effective_row = row if row<=n else n*2 - row 
        spaces = n-effective_row        
        
        for col in range(spaces):
            print(" ",end="")
        for col in range(effective_row,0,-1):
            print(col,end="")
        for col in range(2,effective_row+1):
            print(col,end="")
        print("")
        
def pattern_24(n):
    for row in range(1,n*2+1):
        effective_row = row if row<=n else n*2 - row+1
        stars = effective_row
        spaces = (2*n) - (effective_row*2)
        
        left_star_end = stars
        right_star_start = stars+spaces+1
        
        for col in range(1,n*2+1):
            if col == left_star_end or right_star_start == col or col==1 or col==2*n:
                print("*",end="")
            else:
                print(" ",end="")
        print("")
            

if __name__ == "__main__":
    # pattern_17(5)
    pattern_24(5)