name = "Maksat"
if len(name) < 100:
        list2 = []
        for alpha in name:
            if alpha not in list2:
                list2.append(alpha)
        if len(list2) % 2 == 0:
            print("on")
        else:
            print("ona")