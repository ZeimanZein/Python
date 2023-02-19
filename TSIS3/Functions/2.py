def grad(f):
    return (5 / 9) * (f - 32)


far = int(input())
print(grad(far))