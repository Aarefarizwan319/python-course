my_dict={}

my_dict={'name':'Aliha', 1:[2,3,4]}
my_dict={'name':'Aliha','age': '16','hobby':'Sketching'}
print(my_dict['name'])
print(my_dict.get('age'))
print(my_dict['hobby'])

my_dict['favNovel']='Fourth Wing'
print(my_dict)

my_dict.pop('age')
print(my_dict)

my_dict['favCartoon']='Attack on Titans'
print(my_dict)
