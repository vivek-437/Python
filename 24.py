def print_rangoli(size):
    # your code goes here

    
    # for i in range(1,size):
    #     for j in range(2*(size-i)):
    #         print(end="-")
    #     for j in range(2*(size-i)):
    #         print(end="-")
    #     print()

    for i in range(size-1,0,-1):
        for j in range(2*i):
            print(end="-")
        for j in range(size-1,i-1,-1):
            if i!=(size-1):
                print(chr(65+j).lower(),end="-")
            else:
                print(chr(65+j).lower(),end="")
        for j in range(1,size-i):
            if j!=(size-i-1):
                print(chr(65+j+i).lower(),end="-")
            else:
                print(chr(65+j+i).lower(),end="")

        for j in range(2*i):
            print(end="-")
        print()


    for i in range(size):
        for j in range(2*i):
            print(end="-")
        for j in range(size-1,i-1,-1):
            if i!=(size-1):
                print(chr(65+j).lower(),end="-")
            else:
                print(chr(65+j).lower(),end="")
        for j in range(1,size-i):
            if j!=(size-i-1):
                print(chr(65+j+i).lower(),end="-")
            else:
                print(chr(65+j+i).lower(),end="")

        for j in range(2*i):
            print(end="-")
        



        print()
        























    # your code goes here
    # num=65
    # for i in range(0,size):
    #     for j in range(0,i+1):
    #         ch=chr(num).lower()
    #         print(ch,end="")
    #         num=num+1
    #     print("\r")

    # for i in range(0,size):
        
    #     print(chr(64+size))






if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)






# 5
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
