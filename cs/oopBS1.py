import time


class Test(object):
  ttest = 0

  def __init__(self, name):
    self.name = name
    Test.ttest += 1

  def inc(func):
    def wrapper(*args, **kwargs):
      start = time.time()
      result = func(*args, **kwargs)
      end = time.time()
      print(f"{start} /-/ {end} /-/ {round((end-start)*10000, 10)}")
      return result
    return wrapper

  @classmethod
  def how_many(cls):
    print(f"classmethod how_many: {cls.ttest}")
 
  @staticmethod
  def howMany():
    print(f"staticmethod howMany: {Test.ttest}")

  def __del__(self):
    Test.ttest -= 1
    if Test.ttest == 0:
      print('0')
    else:
      print(f"Total: {Test.ttest}")

  @property
  @inc
  def main(self):
    print("Test")

# -----------------------------------------------------------------------------
# class SchoolMember(object):
class SchoolMember:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print('(Создан SchoolMember: {0})'.format(self.name))

  def tell(self):
    print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
  def __init__(self, name, age, salary):
    # SchoolMember.__init__(self, name, age)
    # super(Teacher, self).__init__(name, age)
    super().__init__(name, age)
    self.salary = salary
    print('(Создан Teacher: {0})'.format(self.name))

  def tell(self):
    # SchoolMember.tell(self)
    super().tell()
    print('Зарплата: "{0:d}"'.format(self.salary))

class Student(SchoolMember):
  def __init__(self, name, age, marks):
    # SchoolMember.__init__(self, name, age)
    # super(Student, self).__init__(name, age)
    super().__init__(name, age)
    self.marks = marks
    print('(Создан Student: {0})'.format(self.name))

  def tell(self):
    # SchoolMember.tell(self)
    super().tell()
    print('Оценки: "{0:d}"'.format(self.marks))


if __name__ == "__main__":
  v = Test('test')
  v.main
  v2 = Test('test')
  del v2
  v.howMany()
  Test.how_many()

  print("# ----------------------------------------------")
  t = Teacher('Mrs. Shrividya', 40, 30000)
  s = Student('Swaroop', 25, 75)

  members = [t, s]
  for member in members:
      member.tell()

  print("# ----------------------------------------------")






