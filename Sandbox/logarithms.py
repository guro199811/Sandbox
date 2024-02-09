import math

def calculate_logarithm(number, base):
    if number <= 0 or base <= 0 or base == 1:
        print("invalid input. Number and base must be positive, and base must not be 1.")
        return None
    result = math.log(number, base)
    return result



while True:
    num_to_log = input('Input Number to log: ')
    log_base = input('Log Base: ')
    result = calculate_logarithm(int(num_to_log), int(log_base))
    if result is not None:
        print(f"the logarithm of {num_to_log} with base {log_base} is: {result}")
    after = input('Do You want to continue? Y/N: ')
    if after.lower() == 'y':
        continue
    elif after.lower() == 'n':
        break
    else:
        continue