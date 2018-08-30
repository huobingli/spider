#-- coding: utf-8 --
from collections import Iterable

def findMinAndMax(L):
    l = len(L)
    if l == 0:
        return (None, None)
    ma = L[0]
    mi = L[-1]
    if l == 1:
        return (mi, ma)
    elif l == 2:
        if ma >= mi:
            return (mi, ma)
        else:
            return (ma, mi)
    else:
        L=L[1:-1]
        for i in L:
            if i>ma:
                ma=i
            if i<mi:
                mi=i
        return (mi,ma)

    return (None, None)

def test():
  if findMinAndMax([]) != (None, None):
    print('测试失败!')
  elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
  elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
  elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
  else:
    print('测试成功!')

if __name__ == '__main__':
    test()