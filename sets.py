kume = {0,1,2,3,4,5}
kume2 = {3,4,5,6,7,8}
kume3 = {9,10,11,12,13,14}

print(kume.difference(kume2)) #Fark
print(kume.intersection(kume2)) #Kesişim
print(kume.isdisjoint(kume3)) #Ayrık mı true
print(kume.isdisjoint(kume2)) #Ayrık mı false
print(kume.union(kume2,kume3)) #Bireşim kümesi
