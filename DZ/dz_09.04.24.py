def count_negative_numbers(arr, n):
    if n == 0:
        return 0
    else:
        count = count_negative_numbers(arr, n - 1)
        if arr[n - 1] < 0:
            return count + 1
        else:
            return count

array = [-2, 3, 8, -11, -4, 6]
size = len(array)

n = count_negative_numbers(array, size)

print(f'n = {n}')
