import time
#count = 0
#while (True):
#    print(count)
#    count += 1
#   time.sleep(0.500)

#count = 0
# while (count <= 10):
#     print('iter = ', count)
#     count += 1
#     time.sleep(0.500)


# count = 0
# iter_count = 1
# while (count <= 10):
#     print(iter_count, '--- iter = ', count)
#     count += 1
#     iter_count += 1
#     time.sleep(0.200)


# count = 0
# iter_count = 1
# while (count <= 10):
#     print(iter_count, '--- iter = ', count)
#     if count == 5:
#         print('Count == ', count)
#     count += 1
#     iter_count += 1
#     time.sleep(0.200)


# как только count = 5, ниже строчки не будет отрабатывать
# count = 0
# iter_count = 1
# while (count <= 10):
#     print(iter_count, '--- iter = ', count)
#     if count == 5:
#         print('Count == ', count)
#         break
#     count += 1
#     iter_count += 1
#     time.sleep(0.200)

# Как только доходит до continue, цикл возвращается обратно к wile и происходит бесконечный цикл
# count = 0
# iter_count = 1
# while (count <= 10):
#         print(iter_count, '--- iter = ', count)
#         if count == 5:
#             print('Count == ', count)
#             continue
#         count += 1
#         iter_count += 1
#         time.sleep(0.500)


# ll = [11, 22, 33, 44]    # Переменная со списком.
# for i in ll:
#     print(i)
#     time.sleep(0.500)


# for i in range(0,10 +1):
#     print(i)
#     time.sleep(0.500)


#ll = [11, 22, 33, 44, 55, ['qq', 'ww', 'ee', 'rr', 'tt', 'yy'], 66, 77] # Когда доходим до списка букв его можно тоже проитерировать.
# for i in ll:
#     print(i)
#     time.sleep(0.500)

# ll = [11, 22, 33, 44, 55, ['qq', 'ww', 'ee', 'rr', 'tt', 'yy'], 66, 77]
# for i in ll:
#     print(i, ll.index(i))
#     time.sleep(0.500)
# print(i) - принтуем элемент, выводим функцию index у списка и скормить ей каждый элемент, i функция вернет индекс этого элемента


# ll = [11, 22, 33, 44, 55, ['qq', 'ww', 'ee', 'rr', 'tt', 'yy'], 66, 77]
# count = 0
# for i in ll:
#     print(count, ll[count])
#     count += 1
#     time.sleep(0.500)


ll = [11, 22, 33, 44, 55, ['qq', 'ww', 'ee', 'rr', 'tt', 'yy'], 66, 77]
count = 0
for i in range(0, ll.length):     #длинна списка
    print(count, ll[count])
    count += 1
    time.sleep(0.500)


