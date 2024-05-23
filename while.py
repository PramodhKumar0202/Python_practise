# while loop = a statement that will execute it's block of code as long as it;s condition is true
name = ""
while len(name) == 0:
    name =input("enter your name: ")
print("welcome to the world "+name)  
# another way doing same program
name =None
while not name:
    name =input("enter your name: ")
print("hello monster"+name)      
