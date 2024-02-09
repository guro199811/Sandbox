nums = []
# s is starting point
s = 1
# f is finishing point
f = 1000

def populateNums(n, count):
    for c in range(count):
        nums.append(n)
        n+=1
    return nums


counter = populateNums(s, f)

primenums = []

def is_prime(num):
    if num == 1:
        return True
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def priming(listofnums):
    for num in listofnums:
        if is_prime(num):
            primenums.append(num)
    return primenums

p = priming(counter)

print(p)
