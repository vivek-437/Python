def swap_case(s):
    l=''
    for i in s:
        if i.isupper():
            l +=i.lower()
        else:
            l +=i.upper()
    return print(l)

swap_case('HackerRank.com presents "Pythonist 2".')