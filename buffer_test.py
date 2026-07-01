dict = {}
dict['a'] = [1]
print(dict)

dict['a'].append(2)
print(dict)

print(len(dict['a']))

list_a = dict['a']
print(list_a)
print(len(list_a))

dict2 = {}
dict2['a'] = 'a'
print(dict2['a'])

dict2.update({'a':['a','b']})
print(dict2['a'])
print(dict2)
