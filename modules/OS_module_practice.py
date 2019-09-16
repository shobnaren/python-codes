import sys
import os


def list_fn(dir):
    filenames = os.listdir(dir)
    print("list filenames:", filenames)
    for filename in filenames:
        path = os.path.join(dir, filename)
        print("path:", path)
        print("PWD:", os.path.abspath(path))
    print(os.path.exists("/home/shobana"))


if __name__ == '__main__':
    list_fn("/home/shobana")




