def test_gen(n):
  while n != 0:
    yield n - 1
    n -= 1

def test_gen2(n):
  s = 0; count = 0
  for i in range(1, n + 1):
    s += 1; count += 10
    yield s / count

def csv_reader(file_name):
  file = open(file_name)
  result = file.read().split("\n")
  return result

def csv_reader_row(file_name):
  for row in open(file_name, 'r'):
    yield row

if __name__ == "__main__":
  # g = test_gen(5)
  # for i in g: print(i)

  # t = test_gen2(10)
  # # for i in t: print(i)
  # print(next(t))
  # print(next(t))

# https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv
  t = csv_reader_row("test.txt") # iris dataset
  _len = len(csv_reader("test.txt"))
  head = next(t)
  print(f"{0}#", head)
  print("-----"*5)

  iters1 = []
  for i in range(50):
    iters1.append(next(t))
    # print(f"{i+1}#", next(t))

  iters2 = []
  for i in range(50):
    iters2.append(next(t))
    # print(f"{i+1}#", next(t))

  iters3 = []
  for i in range(50):
    iters3.append(next(t))
    # print(f"{i+1}#", next(t))
  
print("#######################--####################")

print(iters1, len(iters1))
print(iters2, len(iters2))
print(iters3, len(iters3))

t3 = [*iters1, *iters2, *iters3]
print(t3, len(t3))

print("#######################--####################")
with open('ttest.txt', 'w') as fl:
  print(head)
  fl.write(head)
  for i in t3:
    fl.write(i)
    print(i)

