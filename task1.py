

string = "hello World hi Mike hillary hehehehe"
string1 = string[:string.find('h') + 1]
string2 = string[string.rfind('h'):]
string3 = string[string.find('h') + 1: string.rfind('h')]
string3 = string3.replace('h', 'H')
print(string1 + string3 + string2)