# numbers = list(range(10, 100001, 10))
numbers = [10,20,30,40,50]
search = int(input("what are you searching"))

for i in numbers:
    
    if i == search:
        print("is found")
    else:
        print("not found")


# x=0
# for i in numbers:
#     x+=1
#     if i == search:
#         print(f"{i} found in {x} iterations")
#         break
    


# left = 0
# right = len(numbers) - 1
# x = 0

# while left <= right:
#     middle = (left + right) // 2
#     x += 1

#     if numbers[middle] == search:
#         print(f"{search} found in {x} iterations")
#         break
#     elif numbers[middle] < search:
#         left = middle + 1
#     else:
#         right = middle - 1
# else:
#     print(f"Value not found after {x} iterations")

