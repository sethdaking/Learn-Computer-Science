# 3. Write a program to reverse a string.

def reverse_string(s):
    reversed_str = ""  # Initialize an empty string to store the reversed result
    for i in range(len(s)-1, -1, -1):  # Loop from the end of the string to the beginning
        reversed_str += s[i]  # Add each character to the reversed string
    return reversed_str  
    # return s[::-1]

s = input("Enter a string: ")
s = list(s)

print("Reversed string: ", reverse_string(s))