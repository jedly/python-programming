
def ndigits(x):
    if(x == 0):
        return 0
    if(abs(x) / 10 == 0):
        return 1
    else:
        return 1 + ndigits(x / 10)
