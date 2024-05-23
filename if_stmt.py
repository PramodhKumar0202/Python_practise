# if statement = a block of code that will execute if it's condition is true
age =int(input("how old are you?: "))
if age ==100:
    print("you are an adult!")
elif age <0:
    print("you haven't born yet !")  
elif age >= 18:
    print("you are a century old !")      
else:
    print("you are a child!")    





# logical operators (and,or,not) = used to check two or more conditions
temp =int(input("what is the temprature outside?: "))
if temp>=0 and temp<=24:
    print("temparature is good!")
elif temp <0 or temp < 24:
    print("it's too sunny")
else:
    print("enjoy in home !")        

