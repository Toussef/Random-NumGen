import random

print('Hello! Input a number!')

uInput = int(input())

if uInput == 0:
    e = random.randint(0, 9)
    

else:
    e = random.randint((10 ** (uInput -1)), (10 ** uInput) - 1)
    
print(e)
