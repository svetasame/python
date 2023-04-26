def max1(a,b):
  if a > b:
    return a
  return b
  
# фибоначии


def fibb(n):
  if n in [1, 2]:
    return 1
  # обязательно указываем базис то есть условия выхода
  return fibb(n-1) + fibb(n-2) # сам вызов рекурсии

def quick_sort(array):
  if len(array) <= 1:
    return array # базис рекурсии усл вывода
  else:
    pivot = array [0]
  less = [i for i in array[1:] if i <= pivot]
  greater = [i for i in array[1:] if i > pivot]  
  return quick_sort(less) + [pivot] + quick_sort(greater)


def merge_sort(nums):
  if len(nums) > 1:
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        nums[k] = left[i]
        i += 1
      else:
        nums[k] = right[j]
        j += 1
      k += 1
    while i < len(left):
      nums[k] = left[i]
      i += 1
      k += 1
    while j < len(right):
      nums[k] = right[j]
      j += 1
      k += 1
      
    
      
        