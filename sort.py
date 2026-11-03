import random
list = []#создал пустой список и заполнили его 100 случайными числами от 0 до 1 000 000
for i in range(100):
    list.append(random.randint(0, 1000000))
print("Исходный случайный список:")
print(list)#вывел начальный сгенерированный список в консоль
arr_bubble = []
for x in list:
    arr_bubble.append(x)#создал отдельный список для пузырьковой сортировки, скопировав туда числа по одному
comparisons_bubble = 0  
swapped = True  
step = 1  
print("Старт сортировки пузырьком:")
while swapped:
    swapped = False  #если перестановок в цикле не будет, то swapped останется False и я выйду из цикла.
    for i in range(len(arr_bubble) - 1):
        comparisons_bubble += 1  #увеличиваю счетчик сравнений, так как сейчас будет проверка через "if".
        if arr_bubble[i] < arr_bubble[i + 1]:
            arr_bubble[i], arr_bubble[i + 1] = arr_bubble[i + 1], arr_bubble[i]#знак "<" проверяет, меньше ли текущее число следующего. Если да, меняю их местами для убывающего порядка.
            swapped = True  #ставлю True, сообщая программе, что была перестановка и массив еще не идеально отсортирован.
    print("Шаг пузырька", step, ":", arr_bubble)
    step += 1  #вывожу текущее состояние списка и увеличиваю номер шага на единицу.
arr_selection = []
for x in list:
    arr_selection.append(x)#создал еще один отдельный список для сортировки выбором, чтобы работать с чистыми данными.
comparisons_selection = 0  
step = 1  
n = len(arr_selection)  
print("Старт сортировки выбором:")
for i in range(n):
    max_index = i  #предполагаю, что текущий элемент под индексом "i" — самый большой из оставшихся.
    for j in range(i + 1, n):
        comparisons_selection += 1  #увеличиваю счетчик, так как сейчас сравниваю элементы через "if".
        if arr_selection[j] > arr_selection[max_index]:
            max_index = j  #если нашёл элемент больше, запоминаю его индекс как новый самый максимальный.
    arr_selection[i], arr_selection[max_index] = arr_selection[max_index], arr_selection[i]#поменял местами элемент в начале несортированной части списка и найденный самый большой элемент.
    print("Шаг выбора", step, ":", arr_selection)
    step += 1  #вывожу изменения на этом этапе и увеличиваю номер шага.
print("Отсортированный список (Пузырек):")
print(arr_bubble)
print("Количество сравнений в пузырьковой сортировке:", comparisons_bubble)#вывожу итоговый результат работы первого алгоритма и сумму его сравнений.
print("Отсортированный список (Выбор):")
print(arr_selection)
print("Количество сравнений в сортировке выбором:", comparisons_selection)#вывожу итоговый результат работы второго алгоритма и сумму его сравнений.