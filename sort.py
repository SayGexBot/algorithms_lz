import random
x = 0
l1 = []
c1 = 0
c2 = 0
# создание списка
for i in range(100):
    l1.append(random.randint(1,1000000))
l2 = l1.copy()
# сортировка пузырком
for i in range(len(l1)-1):
  for j in range(len(l1)-i-1):
    if l1[j] < l1[j+1]:
      l1[j+1], l1[j] = l1[j], l1[j+1]
      c1 += 1
      print(l1)
# сортировка выборкой
for a in range(len(l2)):
  mi = a
  for j in range(a+1, len(l2)):
     if l2[j] > l2[mi]:
       mi = j
       c2 += 1
       print(l2)
  l2[mi], l2[a] = l2[a], l2[mi]
  
print(l2, "кол-во шагов сортировки пузырком: ", c1, "кол-во шагов сортировки выборкой: ", c2)