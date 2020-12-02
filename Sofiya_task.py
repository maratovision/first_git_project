with open("spam.txt", "r") as file1:
    file2 = open("dont_read.txt", "w")
    list1 = file1.readlines()
    for line in list1:
        line = line.strip()
        if "HELP" in line or "urgent" in line or "HELP" in line:
            file2.write(line + "\n")
        elif line.isupper() and line.endswith("!!!") or line.isupper() or line.endswith("!!!"):
            file2.write(line + "\n")

    print("Find")
