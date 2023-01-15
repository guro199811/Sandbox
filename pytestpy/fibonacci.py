num_1 = 0
num_2 = 1

try:
    count = int(input("Count: "))
except:
    count = int(input("Please input the whole number: "))
if count == 0:
    count = int(input("Your number is 0, try higher: "))
elif count <= 0:
    count = int(input("Your number is under 0, try higher: "))


print(num_1)
for i in range(count - 1):
    num_3 = num_1 + num_2
    num_1 = num_2
    num_2 = num_3
    print(num_2)