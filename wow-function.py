# We call it 'wow' due to its incredible rate of growth!

def f(k):
    return 2*k

def f2(k):
    return 2**k

def f3(k):
    if k == 1:
        return f2(1)
    else:
        return f2(f3(k-1))

def wow(k):
    if k == 1:
        return f3(1)
    else:
        return f3(wow(k-1))


print(wow(2))
