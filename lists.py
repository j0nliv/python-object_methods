liste = [1,2,3,4,5,6,7,8,9,10]
liste2 = ["a","b","c","d","e"]
liste3 = ["f","g","h"]
liste.append(11) #Listeye eleman ekleme
liste2.extend(liste3) #Listeye başka bir liste ekleme
print(liste.pop()) #Parametre girilirse o indexe ait değeri siler, girilmezse son elemanı siler
liste.remove(7) #Verile parametreyi listeden çıkarır
print(liste.index(2)) #Girilen parametreyi listede taratarak indexini döndürür
print(liste.count(2)) #Girilen parametrenin listede kaç kere geçtiğini döndürür
print(liste.sort()) #Listeyi küçükten büyüğe, string ise alfabetik olarak sıralar
print(liste2.sort(reverse=True)) #Tersten sıralama yaptırır