# Высота забора
h = 5

def count(num_of_friends):
    list1 = []
    for i in range(num_of_friends):
        new_elem = int(input())
        list1.append(new_elem)
    return list1

def vs():
    list1 = count(3)
    y = 0 # Ширина дороги
    for height in list1:
        if height <= h:
            y = y + 1
        else:
            y = y + 2
    print(y)

vs()