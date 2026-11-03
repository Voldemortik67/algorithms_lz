import random
bubble = list()
selection = list()
for i in range(0, 100):# cоздадим список с рандомными значениями
     element = random.randint(1 ,1000)
     bubble.append(element)
     selection.append(element)
check = 0 # с помощью этой переменной будем проверять на своем ли месте элемент
countb = 0 # количество итераций для пузыря
print('Исходный список: ', bubble,'\n') # \n делает переход на новую строку
while True: # сортировка пузырьком
    check = 0
    for i in range(0, len(bubble)-1): 
        if bubble[i] < bubble[i+1]:
            bubble[i], bubble[i+1] = bubble[i+1], bubble[i]   # меняем местами
            print(bubble,'\n')
            check += 1
            countb += 1
    if check == 0: #если инверсий нет, то список отсортирован
        break
print('Исходный список: ', selection,'\n')           
i = 0 # итератор
counts = 0 # количество сравнений
for i in range(0, len(selection)): #сортировка выбором
    first = selection[i]
    for j in range(i, len(selection)):
        if first < selection[j]:
            counts += 1
            first = selection[j]
            itt = j
    selection[i], selection[itt] = first, selection[i]  # меняем местами
    print(selection,'\n')
print('Отсортированный список пузырьком: ', str(bubble)) # вывод
print('Отсортированный список выбором: ', str(selection))
print (f'Количество сравнений в сортировке пузырьком: {countb}')
print (f'Количество сравнений в сортировке выбором: {counts}') 