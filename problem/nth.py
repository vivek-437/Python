# # Enter your code here. Read input from STDIN. Print output to STDOUT
# a,b=map(int,input().split())
# result=0
# for i in range (0,a):
#     m=list(map(int,input().split()))
#     # print(m)
    
    



# n=6
# for i in range(1,n+1):
#     print(' '*(n-i)+'*'*(i))






# arr=[1,2,3,4,5]
# arr=sorted[arr]
# maxresult=sum(arr[-1:-5])
# minresult=sum(arr[0:4])






# arr=[3,1,2,3]

# def birthdaycakecandles(arr):
#     maxe=max(arr)
#     counter=0
#     for i in range(len(arr)):
#         if arr[i]==maxe:
#             count+=1
#     return(counter)





# s="07:05:45PM"
# def timeConversion(s):
#     # Write your code here
#     n= s.split(':')
#     lastone=n[-1]
#     hour=n[0]
#     minute=n[1]
#     second=0
#     ampm=''
#     for i in range(len(lastone)):
#         second=lastone[i:i+2]
#         ampm=lastone[2:]
#         break

#     if int(hour) ==12 and ampm=='AM':
#         hour='00'
#     elif int(hour)<12 and ampm=='PM':
#         hour=12+int(hour)
#     elif int(hour)>12 and ampm=='AM':
#         hour=12-int(hour)    
#     return str(f'{hour}:{minute}:{second}')
# print(timeConversion(s))







# o=[73,67,38,33]

# def gradingStudents(grades):
#     # Write your code here
#     n=0
#     for i in range(grades):
#         n=5*i
#         if n>grades:
#             break
#     if n<40:
#         pass
#     elif n-grades<3:
#         grades=n
#     elif n-grades==3:
#         pass
    
#     return grades 

# for i in range(len(o)):
#     print(gradingStudents(o[i]))
