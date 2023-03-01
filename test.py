from ctypes import *

if __name__ == "__main__":
    foo = CDLL("./foo")

    print(foo.add(50, 50))
