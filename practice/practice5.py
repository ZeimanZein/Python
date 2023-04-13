def get_middle(s):
    result = ""
    middle = int(len(s)//2)
 
    if len (s)% 2 == 0: 
        result = "".join(s[(middle-1):(middle+1)])
    else:
        result = s[middle]
 
    return result


s = input()
 
print(get_middle(s))