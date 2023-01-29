def high_and_low(s):
    num_list = list(map(int,s.split()))
    return max(num_list),min(num_list)
s = input("")
print(high_and_low(s))