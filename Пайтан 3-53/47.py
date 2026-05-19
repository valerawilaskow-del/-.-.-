lst1 = ['a', 'b', 'c']
lst2 = ['d', 'e']
lst1.extend(lst2)
print(lst1)
lst3 = ['a', 'b', 'c']
lst4 = ['d', 'e']
lst5 = [1, 2, 3]
lst3.extend(lst5)
lst3.extend(lst4)
print(lst3)