string = input()
if string.isupper() or string.islower():
    string = string.swapcase()
elif string[0].islower() or string[0].isupper():
    string = string
else:
    string = string.capitalize()
print(string)