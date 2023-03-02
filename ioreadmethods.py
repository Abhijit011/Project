f = open("my2.txt", "r")
while True:
    line = f.readline()
    if not line:
        # print("Completed")
        break
    print(line, type(line))
