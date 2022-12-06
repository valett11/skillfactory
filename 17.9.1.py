sequence = input("Введите последовательность: ")
element = int(input("Введите  любое число: "))


def sort_seq():
    array = list(map(int, sequence.split()))
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def binary_search(array, element, left=0, right=(len(sort_seq()) - 1)):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        if middle < 1:
            print("Для этого числа невозможно установить номер позиции")
        else:
            return middle - 1  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

# запускаем алгоритм на левой и правой границе
print(binary_search(sort_seq(), element))