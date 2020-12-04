#Задача1

# a = str(input('Введите предложение:'))
#
# if a[0].isupper() and a[-1].endswith('.'):
#     print(a)
# elif a[0].islower() and a[-1].endswith('.'):
#     a = a.capitalize()
#     print(a)
# elif a[0].isupper() and not a[-1].endswith('.'):
#     print(a + '.')
# elif a[0].islower() and not a[-1].endswith('.'):
#     a = a.capitalize()
#     print(a + '.')

                    #Задача 3
# a = str(input('Введите свой номер:'))
#
# if len(a) < 14 and a.startswith('+'):
#     print(a)
# elif len(a) < 14 and a.startswith('0'):
#     a = a.replace('0', '', 1)
#     print('+996' + a)
# elif len(a) == 9 and a[0].isdigit():
#     print('+996' + a)

            #Задача 4
# n = int(input())
# i = 1
# sum = 0
#
# while i <= n:
#     sum += i**2
#     i += 1
# print(sum)
                    #Задача 4
a = int(input())
b = int(input())
year = 0
while b > a:
    year += 1
    a = a * 3
    b = b * 2
 print(year)