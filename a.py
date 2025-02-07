def exp(base, aa):
    if len(base) == 0:
        return 0
    if base[0] == aa:
        return 1 + exp(base[1:], aa)
    else:
        return exp(base[1:], aa)
lis = [1, 1, 2, 3, 4]
aa = 1    

print(exp(lis, aa))

