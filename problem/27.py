nshoes=int(input())
shoesize=Counter(map(int,input().split()))
coutshoe=int(input())
income=0
for i in range(countshoe):
    size,price=map(int,input().split())
    if shoesize[size]:
        income+=price
        shoesize[size]-=1
    
print(income)