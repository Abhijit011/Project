# in w mode u canot read files i.e txt of files wont appear
# f = open('my2.txt', 'w')
# print(f)
# text = f.read()
# print(text)
# f.close()
with open('my.txt', 'a') as f:
    # print(f.read())
    for i in range(0, 1000000):
        f.write("hello my name is B \n")
