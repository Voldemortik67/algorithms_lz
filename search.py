import random
unique_numbers = []
while len(unique_numbers) < 100: #цикл крутится, пока не наберется ровно сто штук
    num = random.randint(0, 1000000)
    if num not in unique_numbers: #проверяю на уникальность, операторы членства in/not in
        unique_numbers.append(num)
swapped = True
while swapped: #кручу цикл, пока в массиве есть что переставлять
    swapped = False
    for i in range(len(unique_numbers) - 1): #иду по списку до предпоследнего элемента
        if unique_numbers[i] > unique_numbers[i + 1]: #если левое число больше правого, то они стоят неправильно
            unique_numbers[i], unique_numbers[i + 1] = unique_numbers[i + 1], unique_numbers[i]#меняю элементы местами
            swapped = True 
print("Сгенерирован и отсортирован список из 100 чисел:")
print(unique_numbers)
search_value = int(input("Введите число для поиска: "))#запрашиваю число у пользователя
index_linear = -1 #линейный поиск
comparisons_linear = 0
found_linear = False  #флаг, чтобы знать, нашёл элемент или нет
for i in range(len(unique_numbers)):
    if found_linear == False:#если еще не нашёл число, то продолжаю проверять
        comparisons_linear = comparisons_linear + 1  #считаю, сколько раз сравнил
        if unique_numbers[i] == search_value:
            index_linear = i  #запоминаю индекс, где лежит число
            found_linear = True
first = 0 #бинарный поиск
last = len(unique_numbers) - 1 #начальные границы от нуля до конца списка
index_binary = -1
comparisons_binary = 0
while (first <= last) and (index_binary == -1): #ищу, пока границы не сошлись и пока число не нашлось
    mid = (first + last) // 2 #делю отрезок пополам и округляю в меньшую сторону
    comparisons_binary = comparisons_binary + 1 #считаю +1 сравнение за каждый шаг цикла
    if unique_numbers[mid] == search_value: #если угадал сразу, то сохраняю индекс
        index_binary = mid
    else:
        if search_value < unique_numbers[mid]: #если не совпало, проверяю, в какую сторону двигать границы
            last = mid - 1 #отрезаю правую часть списка
        else:
            first = mid + 1 #отрезаю левую часть списка
if index_linear != -1: #вывожу результат
    print("Элемент найден!")
    print("Индекс элемента в линейном поиске:", index_linear)
    print("Сравнений в линейном поиске:", comparisons_linear)
    print("Индекс элемента в бинарном поиске:", index_binary)
    print("Сравнений в бинарном поиске:", comparisons_binary)
else: #этот блок сработает, если числа вообще нет в списке
    print("Элемент не найден в списке.")
    print("Сравнений в линейном поиске:", comparisons_linear)
    print("Сравнений в бинарном поиске:", comparisons_binary)