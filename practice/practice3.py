import datetime
def get_random():
    date_num=int(datetime.datetime.utcnow().timestamp())
    result = date_num % 10
    if result==0:
        return 1
    return result
def gen(d):
    ans=[]
    a = get_random()
    print(a)
    
    while a>0:
        b=str(d)
        ans.append(b)
        d += datetime.timedelta(days=1)
        a -= 1
    return ans
        
s=str(input())
d=datetime.datetime.strptime(s, "%d-%m-%Y").date()
print(gen(d))