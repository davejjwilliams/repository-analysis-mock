def fact(num):
    if num == 0:
        return 1
    return num * fact(num - 1)

def sq(num):
    return num*num

def even(num):
    return num % 2 == 0

def odd(num):
    return not even(num)