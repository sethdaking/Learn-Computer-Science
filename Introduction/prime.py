def prime (num):
    if num % 2 != 0:
        return False
    elif num % 2 == 0:
        return True

num = input("Enter a number: ")

try: 
    num = int(num)
    print(prime(num))
except:
    print("Invalid input")  # This will print if the input is not a number.