

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

if __name__ == "__main__":
    pattern_17(5)