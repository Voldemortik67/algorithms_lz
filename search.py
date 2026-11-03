import random 
spisok = random.sample(range(1, 1001), 100) # sample делает элементы неповторяющимися
for i in range(len(spisok) - 1): # Сортировка пузырьком
    for j in range(len(spisok) - 1 - i): 
        if spisok[j] > spisok[j+1]: # Если 1 элемент меньше 2 элемента, то выполняет следующие действия
            spisok[j], spisok[j+1] = spisok[j+1], spisok[j] 
print('Отсортированный список:', spisok) 
countlin = 0
countbin = 0
g = 0 
l = len(spisok)-1
index = -1                     
element = int(input('Введите элемент, который хотите найти: ')) 
#Линейный поиск
for i in range(len(spisok)): #Линейный выбор. Перебор всех элементов списка
    countlin += 1 
    if spisok[i] == element: #если найден нужный элемент, то прекращаем поиск
        break 
while (g <= l) and (index == -1): #Бинарный поиск
    mid = (g + l) // 2 
    countbin += 1 
    if spisok[mid] == element: #Если середина списка равна элементу, который ищут
        index = mid #Приравние индекса к середине списка в этом случае
    else: 
        if element < spisok[mid]:
            l = mid -1 
        else:
            g = mid +1
if index == -1: # -1 остается, те элемента не нашлось
    print('Элемента нет в списке. ')
else:
    print('Индекс элемента по линейному поиску: ', i) # вывод
    print('Индекс элемента по бинарному поиску: ', index)
    print('Количество сравнений при линейном: ', countlin)
    print('Количество сравнений при бинарном поиске: ', countbin)