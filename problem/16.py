def mutate_string(string, position, character):
    l=[]
    for i in string:
        l.append(i)
    l[position]=character
    st1=''
    for i in range(len(l)):
        st1+=l[i]
    return st1

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# abracadabra 
# 5 k