def power(n, *args):
    if args:
        return [i**n for i in args]
    else:
        return 'empty'

print(power(3,3,4,5))