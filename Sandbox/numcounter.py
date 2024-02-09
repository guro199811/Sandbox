nums = []
n = 1

def populateNums(n, count):
    for c in range(count):
        nums.append(n)
        n+=1
    return nums


counter = populateNums(n, 100)

print(counter)