for n in range(3,200):
    # Xi list
    X = [-5 + k*(10/n) for k in range(n+1)]
    # f(x)
    def f(x):
        return 1/(x**2+1)
    # Fi list
    Fi = [f(i) for i in X]
    # Li(x)
    def L(i,x):
        L = 1
        for j in range(n+1):
            if i != j:
                Lix = (x - X[j])/(X[i] - X[j])
                L *= Lix
        return L
    # Li list. x = 2
    Li = [L(i,2) for i in range(n+1)]
    # Fi*Li
    FiLi = [x*y for x,y in zip(Fi, Li)]
    # P(2)
    P2 = sum(FiLi)

    Error = abs(P2-f(2))
    print('N: ', n , 'Error: ' , Error)
