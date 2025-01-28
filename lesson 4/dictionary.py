my_dict = {}
my_dict={1:'apple',2:'bat'}
my_dict={'name':'ben', 1:[2,3,4]}
my_dict={'name':'ben','age': '10'}
print(my_dict['name'])
print(my_dict.get('age'))
my_dict['age'] = 27
print(my_dict)
my_dict['address']='Downtown'
print(my_dict)
my_dict.pop('age')
print(my_dict)
print('Address:',my_dict.get('address'))
