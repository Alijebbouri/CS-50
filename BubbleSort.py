def bubble_sort(data):
  n = len(data)
  swapped = True
  while swapped:
    swapped = False
    for i in range(n - 1):
      if data[i] > data[i + 1]:
        data[i], data[i + 1] = data[i + 1], data[i]
        swapped = True
data = [64, 34, 25, 12, 22, 11, 90,13]
bubble_sort(data)
print(f"Sorted data: {data}")
