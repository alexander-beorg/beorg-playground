import time
from random import randint


def ins(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f"{start}, {end}, {round((end-start)+10000000, 8)}")
    return result
  return wrapper

@ins
def t_1(x):
  iters = 0
  for i in range(len(x)-1):
    for z in range(len(x)-1 - i):
      if x[z] > x[z + 1]:
        # print(z, z+1, x[z], x[z + 1])
        x[z], x[z + 1] = x[z + 1], x[z]
      iters+=1
  print(f"{iters}, {x}")

@ins
def t_2(x):
  iters = 0
  while iters < len(x)-1:
    for z in range(len(x)-1):
      if x[z] > x[z + 1]:
        # print(z, z+1, x[z], x[z + 1])
        x[z], x[z + 1] = x[z + 1], x[z]
      iters += 1
  print(f"{iters}, {x}")

class BubbleSort:
    def __init__(self, l: list):
        if isinstance(l, list):
            self.l = l
        else:
            raise ValueError
    
    @property
    @ins
    def bubble_sort(self):
        iters = 0
        last_item = len(self.l) - 1
        for z in range(0, last_item):
            for x in range(0, last_item - z):
                if self.l[x] > self.l[x + 1]:
                  self.l[x], self.l[x + 1] = self.l[x + 1], self.l[x]
                iters += 1
        print(f"{iters}, {self.l}")
    
    @property
    @ins
    def bubble_sort_w(self):
      iters = 0
      while iters < len(self.l)-1:
        for z in range(len(self.l)-1):
          if self.l[z] > self.l[z + 1]:
            # print(z, z+1, x[z], x[z + 1])
            self.l[z], self.l[z + 1] = self.l[z + 1], self.l[z]
          iters += 1
      print(f"{iters}, {self.l}")


if __name__ == "__main__":
  # print(x:=[randint(1, 99) for i in range(10)])
  x = [randint(1, 99) for i in range(10)]
  print(x)

  print("func")
  t_1(x)
  t_2(x)
  print("OOP")
  v = BubbleSort(x)
  v.bubble_sort
  # print(v.l)
  t = BubbleSort(x)
  t.bubble_sort_w
  # print(t.l)
