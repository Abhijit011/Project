a = 100


def glo():
    global a  # access the global variable
    a = 1000
    print(a)
    y = 100  # Local Variable


glo()
print(a)
