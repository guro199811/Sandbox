def multiargfunct(arg1,arg2,arg3):
    print(f"{arg1}, {arg2}, {arg3} - has been accepted...")

try:
    multiargfunct("great")
except:
    multiargfunct("great", "good")  
else:
    multiargfunct("yeah", "nah")
finally:
    print("finished")