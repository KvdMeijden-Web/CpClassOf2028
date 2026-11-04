numbers = list(range(10, 1000000000001, 10))

search = int(input("What are you searching for? "))

x=0
for i in numbers:
    x+=1
    if i == search:
        print(f"{i} found in {x} iterations")
        break

left = 0
right = len(numbers) - 1
x = 0

while left <= right:
    middle = (left + right) // 2
    x += 1

    if numbers[middle] == search:
        print(f"{search} found in {x} iterations")
        break
    elif numbers[middle] < search:
        left = middle + 1
    else:
        right = middle - 1
else:
    print(f"Value not found after {x} iterations")

