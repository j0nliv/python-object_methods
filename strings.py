kelime = "python"
kelime2 = "PYTHON"
print(kelime.upper()) #Karakterleri büyültür
print(kelime2.lower()) #Karakterleri küçültür
print(kelime2.replace("ON","10")) #Verilen ilk parametreyi metin içerisinde aratarak ikinci parametre ile değiştirir.
print(kelime.startswith("p")) #Verilen parametre ile başlıyorsa
print(kelime.endswith("z")) #Verilen parametre ile bitiyorsa
print("samet emiroglu".split(" ")) #Parametreye göre string parçalara ayrılır, bu parçalar listeye atılır.
print(kelime.strip("p")) #Stringin başında veya sonunda verilen parametre varsa siler
print(kelime.lstrip("p")) #Stringin başında verilen parametre varsa siler
print(kelime.rstrip("n")) #Stringin sonunda verilen parametre varsa siler
print(".".join(["T","C"])) #Liste elemanlarını string ile birleştirir
print(kelime.count("t")) #Parametre olarak verilen değeri string içerisinde sayar
print(kelime.count("t",4)) #İlk parametreyi verilen ikinci parametredeki index değerinden itibaren saydırır
print(kelime.find("y")) #Verilen parametreyi string içerisinde arar ve index değerini döndürür.
print(kelime.rfind("y")) #Verilen parametreyi  string içerisinde sondan itibaren aramaya başlar ve index değerini döndürür