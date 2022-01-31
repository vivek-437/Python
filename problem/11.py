if __name__ == '__main__':
    n = int(input())
    arr = [2 ,3 ,6 ,6 ,5]
    z=max(arr)
    while max(arr)==z:
        arr.remove(max(arr))
    print(max(arr))
