def minion_game(string):
    # your code goes here
    stuart=0
    kevin=0

    for i in range(len(string)):
        if string[i]=='A' or string[i]=='E' or string[i]=='I' or string[i]=='O' or string[i]=='U':
            kevin+=len(string)-i
        else:
            stuart+=len(string)-i
        
    if stuart==kevin:
        print("Draw")
    elif kevin>stuart:
        print(f'Kevin {stuart}')
    else:
        print(f'Stuart {kevin}')



    return

if __name__ == '__main__':
    s = input()
    minion_game(s)