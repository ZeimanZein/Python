import datetime
import json
def get_random(num=1):
    date_num=int(datetime.datetime.utcnow().timestamp())
    result = date_num % 10
    if result==0:
        return 1
    return int(result)
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



names = ["math", "geo", "art", "history","algorithm"]
dates = gen(d)
class lesson:
    def _init_(self, name, d):
        self.names = name
        self.dates = d

lessons = []
for i in range(0,len(dates)):
    w = get_random[i+1]
    x = lesson(names[w],dates[i])
    lessons.append(x)
    lessons[i].print()
print(lessons)