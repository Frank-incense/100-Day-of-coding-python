import random 

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
new_list = {name:random.randint(1,100) for name in names}
passlist = {key:value for key,value in new_list.items() if value > 60}
print(passlist)