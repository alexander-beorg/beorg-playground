import time


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
        # print(z, z+1)
        # print(x[z], x[z + 1])
        x[z], x[z + 1] = x[z + 1], x[z]
      iters+=1
  print(iters)
  print(x)

@ins
def t_2(x):
  iters = 0
  while iters < len(x)-1:
    for z in range(len(x)-1):
      if x[z] > x[z + 1]:
        # print(z, z+1)
        # print(x[z], x[z + 1])
        x[z], x[z + 1] = x[z + 1], x[z]
      iters += 1
  print(iters)
  print(x)

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
        print(iters)
        print(self.l)

    @property
    @ins
    def bubble_sort_w(self):
      iters = 0
      while iters < len(self.l)-1:
        for z in range(len(self.l)-1):
          if self.l[z] > self.l[z + 1]:
            # print(z, z+1)
            # print(x[z], x[z + 1])
            self.l[z], self.l[z + 1] = self.l[z + 1], self.l[z]
          iters += 1
      print(iters)
      print(self.l)


if __name__ == "__main__":
  x = [10, 6, 12, 4, 3, 8, 2, 1]

  # func
  print("func")
  t_1(x)
  t_2(x)

  # oop
  print("\nOOP")
  v = BubbleSort(x)
  v.bubble_sort
  # print(v.l)

  t = BubbleSort(x)
  t.bubble_sort_w
  # print(t.l)


###################################################################
# func
# 28
# [1, 2, 3, 4, 6, 8, 10, 12]
# 1611222175.3873386, 1611222175.387401, 10000000.00006247
# 7
# [1, 2, 3, 4, 6, 8, 10, 12]
# 1611222175.3874433, 1611222175.3874779, 10000000.00003457
#
# OOP
# 28
# [1, 2, 3, 4, 6, 8, 10, 12]
# 1611222175.3875327, 1611222175.38761, 10000000.00007725
# 7
# [1, 2, 3, 4, 6, 8, 10, 12]
# 1611222175.3876426, 1611222175.3876843, 10000000.00004172
###################################################################

