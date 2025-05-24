# data_store.py

numbers_list = []
hash_table = {}

def add_number_to_list(num):
    numbers_list.append(num)

def add_to_hash_table(key, value):
    hash_table[key] = value

def search_in_list(num):
    sorted_list = sorted(numbers_list)
    return binary_search(sorted_list, num), sorted_list

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def edit_hash_table(key, new_value):
    if key in hash_table:
        hash_table[key] = new_value
        return True
    return False

def delete_from_list(num):
    if num in numbers_list:
        numbers_list.remove(num)

def delete_from_hash_table(key):
    if key in hash_table:
        del hash_table[key]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
