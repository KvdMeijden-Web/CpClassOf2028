import random

breakfast = [["banana","cherry","kiwi"], 
             ["milk","orange jus","thee"], 
             ["bread","cornflakes"]]



fruit = breakfast[(random.randint(1,len(breakfast[0]))-1)]
drink = (random.randint(1,len(breakfast[1]))-1)
carb = (random.randint(1,len(breakfast[2]))-1)
print(fruit + ", " +drink+ " and "+carb)
