import random
comp_num = random.sample([0,1,2,3,4,5,6,7,8,9], 4)
print("Число компа: ", comp_num)

guess = list(map(int, input("Ваше число: ")))
print(guess)

bulls = 0
cows = 0

for x in range(len(comp_num)):
    if x in guess and comp_num.index(x) == guess.index(x):
        bulls += 1
    if x not in guess and comp_num[x] == guess[0]:
        cows += 1
print("Быков: ", bulls)
print("Коров:", cows)
