# runner up score
# 3/10 failed



if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    sort=sorted(arr)
    if arr.count(n):
        print(n)
    else:
        sort.remove(max(sort))
        print(max(sort))

    

