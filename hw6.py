def bubble_sort(arr):
    """
    Сортировка списка методом пузырька.
    :param arr: Список для сортировки
    :return: Отсортированный список
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    """
    Сортировка списка методом выбора.
    :param arr: Список для сортировки
    :return: Отсортированный список
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def binary_search(element, arr):
    """
    Поиск элемента в отсортированном списке методом двоичного поиска.
    :param element: Элемент для поиска
    :param arr: Отсортированный список
    :return: None
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == element:
            print(f"Элемент {element} найден на индексе {mid}.")
            return
        elif arr[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    print(f"Элемент {element} не найден в списке.")

# Пример использования:
# Исходный неотсортированный список
unsorted_list = [64, 34, 25, 12, 22, 11, 90]

# Сортировка (можно использовать либо bubble_sort, либо selection_sort)
sorted_list = bubble_sort(unsorted_list.copy())
print("Отсортированный список (пузырьковая сортировка):", sorted_list)

# Двоичный поиск
binary_search(25, sorted_list)
