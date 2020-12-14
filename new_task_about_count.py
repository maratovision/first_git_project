list1 = [1,2,3,4,5,6,7,8,9,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4]

dict1 = {}

for i in range(len(list1)):
    dict1[list1[i]] = list1.count(list1[i])
print(dict1)
