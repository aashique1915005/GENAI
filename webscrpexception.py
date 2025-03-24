new_list = [2,4,6,'California']

# for item in new_list:
#     print(item/2)

for item in new_list:
    try:
        print(item/2)
    except:
        print("The element is not number")


n = 6
while n > 0:
    print(n)
    n = n-2
    if n==2:
        break
print('Hello There !! ')

