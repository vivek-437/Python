
def solve(s):
    str1=""
    space=True
    for x in s :
        if space and x!=' ':
            str1=str1+x.upper() 
            space=False
        elif x==' ':
            str1=str1+x
            space=True
        else :
            str1=str1+x
                    
    return str1 

print(solve("chris alan"))
