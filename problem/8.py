# nested-list
if __name__ == '__main__':
    dict=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dict.append([name,score])
        print(max(dict,key=dict.get))

