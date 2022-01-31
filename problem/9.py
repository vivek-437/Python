if __name__ == '__main__':
    N = int(input())
    L=[]
    i=0
    try:
        while(N>i):
            nsplit = input().split()
            i=i+1
            if nsplit[0] =="append":
                L.append(int(nsplit[1]))
            elif nsplit[0]=="pop":
                L.pop()
            elif   nsplit[0]=="remove":
                L.remove(int(nsplit[1]))
            elif nsplit[0]=="insert":
                L.insert(int(nsplit[1]),int(nsplit[2]))
            elif nsplit[0]=="sort":
                L.sort()
            elif nsplit[0]=="reverse":
                L.reverse()
            elif nsplit[0]=="print":
                print(L)
                i=i-1
    except:
        pass
        
        
        
        
        
        
        
        
        
        
 