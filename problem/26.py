def merge_the_tools(string, k):
    # your code goes here
    i=0
    while i<len(string):
            a=string[i:i+k]
            output=''
            for x in a:
                if x not in output:
                    output+=x
            print(output)
            i+=k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)