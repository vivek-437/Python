# door mat

N,M=map(int, input().split())
n=int((N-1)/2)
m=int((M-7)/2)
for i in range(n,0,-1):
    for j in range(3*i):
        print(end='-')
    for j in range(2*(n-i)+1):
        print(end='.|.')    
    for j in range(3*i):
        print(end='-')
    print()

for i in range(1,2):
    for j in range(m):
        print(end='-')
    for j in range(1):
        print(end='WELCOME')
    for j in range(m):
        print(end='-')
    print()
for i in range(1,n+1,1):
    for j in range(3*i):
        print(end='-')
    for j in range(2*(n-i)+1):
        print(end='.|.')
    for j in range(3*i):
        print(end='-')
    print()



# 9 27
# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------
