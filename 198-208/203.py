#1
def fun(tst1, tst2, tst3):
    return tst1 + tst2 + tst3
tst1 = 2
tst2 = 4
tst3 = 6
print(fun(tst1,tst2,tst3))
#2
def func(lst):
    sum = 0
    for el in lst:
        sum += el
    return sum

tst = [1, 3, 6]

result = func(tst)
print(result)