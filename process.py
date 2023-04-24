from multiprocessing import Process
import os

# 자식 프로세스 생성 
def foo():
    print('This is foo')
    print("my pid is", os.getpid())


def bar():
    print('This is bar')
    print("my pid is", os.getpid())


def baz():
    print('This is baz')
    print("my pid is", os.getpid())
    

if __name__ == '__main__': #현재 모듈이 메인 모듈일 경우 아래 코드가 실행
  print("parent process", os.getpid())
  child1 = Process(target=foo).start() 
  child2 = Process(target=foo).start()
  child3 = Process(target=foo).start()
  