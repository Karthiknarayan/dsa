# rules for creating patterb
#     1. no of lines = no of rows
#     2. find no of columns and that is the j th row, somehow find the relation bw first eow and this
#     3. always print in the inside row/rows
#     4. observation

def pattern1(n):
    for i in range(0,n):
        for j in range(0,i):
            print(j+1,end="")
        print("")

def pattern2(n):
    for i in range(0,n):
        for j in range(0,n-i):
            print(j+1,end="")
        print("")

def pattern3(n):
    for i in range(0,n):
        for j in range(0,n-i):
            print(" ",end="")
        for k in range (0,2*i+1):
            print("*",end="")
        for l in range(0,n-i):
            print("",end="")
        print("")

def pattern4(n):
    for i in range(0,n):
        for j in range(0,i):
            print(" ",end="")
        for j in range(0,n*2-(i*2+1)):
            print("*",end="")
        for j in range(0,i):
            print(" ",end="")
        print("")

def pattern4n5(n):
    for i in range(0,n):
        for j in range(0,n-i):
            print(" ",end="")
        for j in range(0,2*i+1):
            print("*",end="")
        for j in range(0,n-i):
            print(" ",end="")
        print("")
    for i in range(1,n):
        for j in range(0,i+1):
            print(" ",end="")
        for j in range(0,2*(n-i)-1):
            print("*",end="")
        for j in range(0,i):
            print(" ",end="")
        print("")

#pattern1(6)
# 1
# 12
# 123
# 1234
# 12345


#pattern2(5)
# 12345
# 1234
# 123
# 12
# 1

#pattern3(5)
 
#     *    
#    ***    
#   *****    


pattern4n5(5)
# *********
#  ******* 
#   *****  
#    ***   
#     *    