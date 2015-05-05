dict = {'name1':'value1',
              'name2':'value2'}

print(dict.keys())

print(dict.values())

for name in dict.keys():
    print(name + ' has ' +dict[name])
    
print(dict.get('name1'))

dict['name1'] = ['value1', 'valuenew']

print(dict.get('name1'))

dict['name3'] = 'value3'

print(dict)

dict.pop('name3')

print(dict)