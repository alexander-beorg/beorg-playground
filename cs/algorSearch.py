def LinearSearch(lys, element):
  for i in range(len(lys)):
    if lys[i] == element:
      return i
  return -1

def BinarySearch(lys, val):
  first = 0
  last = len(lys)-1
  index = -1
  while (first <= last) and (index == -1):
    mid = (first+last)//2
    if lys[mid] == val:
      index = mid
    else:
      if val<lys[mid]:
        last = mid -1
      else:
        first = mid +1
  return index

import math
def JumpSearch (lys, val):
  length = len(lys)
  jump = int(math.sqrt(length))
  left, right = 0, 0
  while left < length and lys[left] <= val:
    right = min(length - 1, left + jump)
    if lys[left] <= val and lys[right] >= val:
      break
    left += jump
  if left >= length or lys[left] > val:
    return -1
  right = min(length - 1, right)
  i = left
  while i <= right and lys[i] <= val:
    if lys[i] == val:
      return i
    i += 1
  return -1

def FibonacciSearch(lys, val):
  fibM_minus_2 = 0
  fibM_minus_1 = 1
  fibM = fibM_minus_1 + fibM_minus_2
  while (fibM < len(lys)):
    fibM_minus_2 = fibM_minus_1
    fibM_minus_1 = fibM
    fibM = fibM_minus_1 + fibM_minus_2
  index = -1
  while (fibM > 1):
    i = min(index + fibM_minus_2, (len(lys)-1))
    if (lys[i] < val):
      fibM = fibM_minus_1
      fibM_minus_1 = fibM_minus_2
      fibM_minus_2 = fibM - fibM_minus_1
      index = i
    elif (lys[i] > val):
      fibM = fibM_minus_2
      fibM_minus_1 = fibM_minus_1 - fibM_minus_2
      fibM_minus_2 = fibM - fibM_minus_1
    else :
      return i
  if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1] == val):
    return index+1
  return -1

def ExponentialSearch(lys, val):
  if lys[0] == val:
    return 0
  index = 1
  while index < len(lys) and lys[index] <= val:
    index = index * 2
  return BinarySearch( lys[:min(index, len(lys))], val)

def InterpolationSearch(lys, val):
  low = 0
  high = (len(lys) - 1)
  while low <= high and val >= lys[low] and val <= lys[high]:
    index = low + int(((float(high - low) / ( lys[high] - lys[low])) * ( val - lys[low])))
    if lys[index] == val:
      return index
    if lys[index] < val:
      low = index + 1
    else:
      high = index - 1
  return -1

def bubble_sort(nums):  
  # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
  swapped = True
  while swapped:
    swapped = False
    for i in range(len(nums) - 1):
      if nums[i] > nums[i + 1]:
        # Меняем элементы
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
        # Устанавливаем swapped в True для следующей итерации
        swapped = True

def selection_sort(nums):  
  # Значение i соответствует кол-ву отсортированных значений
  for i in range(len(nums)):
    # Исходно считаем наименьшим первый элемент
    lowest_value_index = i
    # Этот цикл перебирает несортированные элементы
    for j in range(i + 1, len(nums)):
      if nums[j] < nums[lowest_value_index]:
        lowest_value_index = j
    # Самый маленький элемент меняем с первым в списке
    nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

def insertion_sort(nums):  
  # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
  for i in range(1, len(nums)):
    item_to_insert = nums[i]
    # Сохраняем ссылку на индекс предыдущего элемента
    j = i - 1
    # Элементы отсортированного сегмента перемещаем вперёд, если они больше
    # элемента для вставки
    while j >= 0 and nums[j] > item_to_insert:
      nums[j + 1] = nums[j]
      j -= 1
    # Вставляем элемент
    nums[j + 1] = item_to_insert


#<
def heapify(nums, heap_size, root_index):  
  # Индекс наибольшего элемента считаем корневым индексом
  largest = root_index
  left_child = (2 * root_index) + 1
  right_child = (2 * root_index) + 2

  # Если левый потомок корня — допустимый индекс, а элемент больше,
  # чем текущий наибольший, обновляем наибольший элемент
  if left_child < heap_size and nums[left_child] > nums[largest]:
    largest = left_child

  # То же самое для правого потомка корня
  if right_child < heap_size and nums[right_child] > nums[largest]:
    largest = right_child

  # Если наибольший элемент больше не корневой, они меняются местами
  if largest != root_index:
    nums[root_index], nums[largest] = nums[largest], nums[root_index]
    # Heapify the new root element to ensure it's the largest
    heapify(nums, heap_size, largest)

def heap_sort(nums):  
  n = len(nums)

  # Создаём Max Heap из списка
  # Второй аргумент означает остановку алгоритма перед элементом -1, т.е.
  # перед первым элементом списка
  # 3-й аргумент означает повторный проход по списку в обратном направлении, 
  # уменьшая счётчик i на 1 
  for i in range(n, -1, -1):
    heapify(nums, n, i)

  # Перемещаем корень Max Heap в конец списка
  for i in range(n - 1, 0, -1):
    nums[i], nums[0] = nums[0], nums[i]
    heapify(nums, i, 0)
#>


#<
def merge(left_list, right_list):  
  sorted_list = []
  left_list_index = right_list_index = 0

  # Длина списков часто используется, поэтому создадим переменные для удобства
  left_list_length, right_list_length = len(left_list), len(right_list)

  for _ in range(left_list_length + right_list_length):
    if left_list_index < left_list_length and right_list_index < right_list_length:
      # Сравниваем первые элементы в начале каждого списка
      # Если первый элемент левого подсписка меньше, добавляем его
      # в отсортированный массив
      if left_list[left_list_index] <= right_list[right_list_index]:
        sorted_list.append(left_list[left_list_index])
        left_list_index += 1
      # Если первый элемент правого подсписка меньше, добавляем его
      # в отсортированный массив
      else:
        sorted_list.append(right_list[right_list_index])
        right_list_index += 1

    # Если достигнут конец левого списка, элементы правого списка
    # добавляем в конец результирующего списка
    elif left_list_index == left_list_length:
      sorted_list.append(right_list[right_list_index])
      right_list_index += 1
    # Если достигнут конец правого списка, элементы левого списка
    # добавляем в отсортированный массив
    elif right_list_index == right_list_length:
      sorted_list.append(left_list[left_list_index])
      left_list_index += 1
  return sorted_list

def merge_sort(nums):  
  # Возвращаем список, если он состоит из одного элемента
  if len(nums) <= 1:
    return nums

  # Для того чтобы найти середину списка, используем деление без остатка
  # Индексы должны быть integer
  mid = len(nums) // 2

  # Сортируем и объединяем подсписки
  left_list = merge_sort(nums[:mid])
  right_list = merge_sort(nums[mid:])

  # Объединяем отсортированные списки в результирующий
  return merge(left_list, right_list)
#>


#<
def partition(nums, low, high):  
  # Выбираем средний элемент в качестве опорного
  # Также возможен выбор первого, последнего
  # или произвольного элементов в качестве опорного
  pivot = nums[(low + high) // 2]
  i = low - 1
  j = high + 1
  while True:
    i += 1
    while nums[i] < pivot:
      i += 1

    j -= 1
    while nums[j] > pivot:
      j -= 1

    if i >= j:
      return j

    # Если элемент с индексом i (слева от опорного) больше, чем
    # элемент с индексом j (справа от опорного), меняем их местами
    nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):  
  # Создадим вспомогательную функцию, которая вызывается рекурсивно
  def _quick_sort(items, low, high):
    if low < high:
      # This is the index after the pivot, where our lists are split
      split_index = partition(items, low, high)
      _quick_sort(items, low, split_index)
      _quick_sort(items, split_index + 1, high)

  _quick_sort(nums, 0, len(nums) - 1)
#>


if __name__ == "__main__":
  # algorSearch
  # https://techrocks.ru/2020/08/12/python-search-algorithms/
  print(LinearSearch([1,2,3,4,5,2,1], 2)) # 1
  print(BinarySearch([10,20,30,40,50], 20)) # 1
  print(JumpSearch([1,2,3,4,5,6,7,8,9], 5)) # 4
  print(FibonacciSearch([1,2,3,4,5,6,7,8,9,10,11], 6)) # 5
  print(ExponentialSearch([1,2,3,4,5,6,7,8],3)) # 2
  print(InterpolationSearch([1,2,3,4,5,6,7,8], 6)) # 5

  
  # import time
  # start = time.time()
  # # вызовите здесь функцию
  # end = time.time()
  # print(start-end)


  # algorSort
  # https://tproger.ru/translations/sorting-algorithms-in-python/
  random_list_of_nums = [5, 2, 1, 8, 4]  
  bubble_sort(random_list_of_nums)  
  print(random_list_of_nums)

  random_list_of_nums = [12, 8, 3, 20, 11]  
  selection_sort(random_list_of_nums)  
  print(random_list_of_nums)

  random_list_of_nums = [9, 1, 15, 28, 6]  
  insertion_sort(random_list_of_nums)  
  print(random_list_of_nums)

  random_list_of_nums = [35, 12, 43, 8, 51]  
  heap_sort(random_list_of_nums)  
  print(random_list_of_nums)

  random_list_of_nums = [120, 45, 68, 250, 176]  
  random_list_of_nums = merge_sort(random_list_of_nums)  
  print(random_list_of_nums)

  random_list_of_nums = [22, 5, 1, 18, 99]  
  quick_sort(random_list_of_nums)  
  print(random_list_of_nums) 

  #
  apples_eaten_a_day = [2, 1, 1, 3, 1, 2, 2]
  apples_eaten_a_day.sort()
  print(apples_eaten_a_day)

  apples_eaten_a_day_2 = [2, 1, 1, 3, 1, 2, 2]
  sorted_apples = sorted(apples_eaten_a_day_2)
  print(sorted_apples)

  #<
  # Обратная сортировка списка на месте
  apples_eaten_a_day.sort(reverse=True)
  print(apples_eaten_a_day)

  # Обратная сортировка, чтобы получить новый список
  sorted_apples_desc = sorted(apples_eaten_a_day_2, reverse=True)
  print(sorted_apples_desc)
  #>
