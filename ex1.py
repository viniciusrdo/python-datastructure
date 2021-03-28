def numReturn(x,y):
    z = int(x) * int(y)
    if z > 1000:
        a = int(x) + int(y)
        return a
    else:
        return z


num1 = input('Insert the first num: ')

num2 = input('Insert the second num: ')

print(numReturn(num1,num2))