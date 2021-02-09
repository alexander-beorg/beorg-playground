import time
from random import randint
# from indfile import ind

# def ind(func):
#   def wrapper(*args, **kwargs):
#     start = time.time()
#     result = func(*args, **kwargs)
#     end = time.time()
#     print(f"{start}-{end}={round((end-start)*10000, 5)}")
#     return result
#   return wrapper

class Boolean_filter:
  def __init__(self, l:list):
    if isinstance(l, list):
      self.l = l
    else:
      raise ValueError

  def ind(func):
    def wrapper(*args, **kwargs):
      start = time.time()
      result = func(*args, **kwargs)
      end = time.time()
      print(f"{start}-{end}={(end-start)*10000}")
      return result
    return wrapper

  @property
  @ind
  def boolean_filter(self):  
    f = []
    swapped = True
    while swapped:
      swapped = False
      for i in range(len(self.l)):
        if (self.l[i] % 2 == 0):
          f.append(self.l[i])
          if self.l[i] not in f:
            swapped = True
    return f


if __name__ == "__main__":
  x = [randint(1, 99) for i in range(10)]
  print(x)

  f = Boolean_filter(x)
  t = f.boolean_filter
  print(t)
  
