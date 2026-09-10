import random

breakfast =[["berry","apple","pineapple"],
            ["yoghurt","milk","buttermilk"],
            ["bread","cornflakes"]]
lengthFruit= len(breakfast[0])-1
randomFruit=random.randint(0,lengthFruit)
print(breakfast[0][randomFruit])
