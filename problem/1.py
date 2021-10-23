# if-else
a="Not Weird"
b="Weird"

if __name__ == '__main__':
    n = int(input().strip())
    if (n%2)!=0:
        print(b)
    elif n>=2 and n<=5:
        print(a)
    elif n>=6 and n<=20:
        print(b)
    elif n>20:
        print(a)
