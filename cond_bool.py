language ='python'

if True:
    print('conditional aws true')
if language == 'python': # checking equal
    print('True')
elif language=='Go':
    print('go')    
else:
    print('no match')
user='admin'
logged_in =True

if user == 'admin' and logged_in:
    print('page')
else:
    print('bad creds')
if not logged_in:
    print('login in')
else:
    print('welcome')
a =[1,2,3,4,5,6]
b =[1,2,3,4,5,6]
print(a==b)# true
print(a is b) # false bcz they addresses are diff
print(id(a))
print(id(b))
print(id(a)==id(b))
condition ='true'
if condition:
    print('pass')
else:
    print('return')
# false values 
# false
#none
#zero of any numeric type
#any empty sequence. for example,'',(),[]
#any empty mapping. for example,{}
                        