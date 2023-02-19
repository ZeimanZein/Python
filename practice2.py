import datetime
def get_random(number):
    date_num=int(datetime.datetime.utcnow().timestamp())
    result = date_num % 10
    if result==0:
        return 1
    return result
number = int(input())
print(get_random(number))
