import threading
import os


def foo():
    print('This is foo')
    print("my pid is", os.getpid())


def bar():
    print('This is bar')
    print("my pid is", os.getpid())


def baz():
    print('This is baz')
    print("my pid is", os.getpid())


if __name__ == '__main__':
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=bar).start()
    thread3 = threading.Thread(target=baz).start()