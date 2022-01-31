total=[]
for _ in range(int(input())):
    total.append([input(),float(input())])

# sorting the list use second variable
sortedtotal=sorted(total,key=lambda x:x[1]);
# to start form second index range
for i in range(1,len(sortedtotal)):
    if(sortedtotal[i][1] != sortedtotal [i+1] [1]):
        score=sortedtotal[i][1]
        break
lst=sorted(sortedtotal)
for x in range(len(lst)):
    if(lst[x][1]==score):
        print(lst[x][0])



