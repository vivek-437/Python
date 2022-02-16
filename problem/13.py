if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    x=student_marks[query_name]
    totalnum=0
    for i in x:
        totalnum+=i
    print ("%.2f" % round(totalnum/len(x),2)) 

# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
