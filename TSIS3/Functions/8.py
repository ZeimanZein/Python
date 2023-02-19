def spy_game(nums):
    ls = []
    final = [0,0,7]
    z =0
    for x in nums:
        if x != 7 and x == 0:
            ls.append(x)
            z = len(ls)
        elif x == 7:
            ls.append(x)
    return  ls[z-2:z+1] == final

print(spy_game([int(n) for n in input().split()]))