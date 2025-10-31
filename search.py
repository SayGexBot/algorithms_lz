import random
l1 = []
c1 = 0
c2 = 0
# создание списка
for i in range(1000000):
    l1.append(i+1)
l1 = sorted(random.sample(l1, 100))
print(l1)
inp = int(input("введите элемент: "))
# линейный поиск
for i in range(len(l1)):
    if l1[i] == inp:
      break
    c1 += 1
else:
   print("недопустимое значение")
# бинарный поиск 
left = 0
right = len(l1) - 1
while left <= right:
    mid = (left + right) // 2
    if l1[mid] == inp:
      print("индекс элемента: ", mid,",","кол-во ходов линейного поиска: ", c1,",","кол-во ходов бинарного поиска: ", c2)
    if l1[mid] < inp:
      left = mid + 1
    else:
      right = mid - 1
    c2 += 1

       
