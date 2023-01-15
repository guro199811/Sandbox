from ast import Break
import time


operation = input("please use either of the options below \n asc (ascend the list)\n desc (Descend The list)\n none (Quit the program)\n: ")

lst = [2, 5, 3, 4, 6, 7, 9]

def ascend(a):
    a.sort()
    return a
def descend(a):
    a.sort()
    a.reverse()
    return a

while True:
    try:
        if operation == "asc":
            print(ascend(lst))
            
        elif operation == "desc":
            print(descend(lst))
            
        elif operation == "none":
            print("Thanks for using this program.)")
            break
        else:
            operation = input("Your INPUT Was Incorrect \n please use either of the options below \n asc (ascend the list)\n desc (Descend The list)\n none (Quit the program)\n: ")
            continue
    except:
        print("Something went wrong, stopping the program ")
        break
    time.sleep(1)
    operation = input("continue? \n asc (ascend the list)\n desc (Descend The list)\n none (Quit the program)\n: ")


