def merge_sort(data):
  """
  Sorts a list in ascending order using the merge sort algorithm.

  Args:
      data: A list of comparable elements.

  Returns:
      A new list containing the sorted elements of the input list.
  """
  if len(data) <= 1:
    return data

  mid = len(data) // 2
  left = merge_sort(data[:mid])
  right = merge_sort(data[mid:])

  return merge(left, right)

def merge(left, right):
  """
  Merges two sorted lists into a single sorted list.

  Args:
      left: A sorted list.
      right: A sorted list.

  Returns:
      A new list containing the merged elements of the input lists.
  """
  merged = []
  i, j = 0, 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1

  merged.extend(left[i:])
  merged.extend(right[j:])

  return merged

# Example usage
unsorted_data = [6, 5, 3, 1, 8, 7, 2, 4]
sorted_data = merge_sort(unsorted_data)

print("Unsorted:", unsorted_data)
print("Sorted:", sorted_data)
