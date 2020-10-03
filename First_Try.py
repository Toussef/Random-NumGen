#Generate a random number based on the number given on the user. Up to 5 charecters. For now
import random
print("Hello!\nInput the number of numbers you'd like to see as the output!(up to 5 numbers)")
uInput = int(input())
if uInput == 0:
    print("I guess you don't need a number :p")
    
elif uInput == 1:
    a = random.randint(0,9)
    print(a)

elif uInput == 2:
    b = random.randint(10,99)
    print(b)

elif uInput == 3:
    c = random.randint(100,999)
    print(c)
    
elif uInput == 4:
    d = random.randint(1000,9999)
    print(d)

elif uInput == 5:
    e = random.randint(10000,99999)    
    print(e)
    
print('Peace')
