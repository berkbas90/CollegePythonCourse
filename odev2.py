dizi = [ [2020,"Ocak",300],[2020,"Şubat",500],[2020,"Mart",250],
         [2021,"Ocak",380],[2021,"Şubat",470],[2021,"Mart",350],
         [2022,"Ocak",350],[2022,"Şubat",450],[2022,"Mart",750]  
       ]

# Cevap 1
tmp = []
indice=0
last=0

for i in range(len(dizi)):
    tmp.append(dizi[i][2])

tmp.sort()


for j in range(len(dizi)):
    if(dizi[j][2]==tmp[0]):
        indice=j
    elif(dizi[j][2]==max(tmp)):
        last=j 

# print(last)

print(f"En küçük değere sahip olan {dizi[indice]}")
print(f"En büyük değere sahip olan {dizi[last]}")

# Cevap 2
sum=0
for b in range(len(dizi)):
    sum=sum+(dizi[b][2])
print("Aritmetik Ortalama",sum/len(dizi))

# Cevap 3

sum=0
count=0
for i in range(len(dizi)):
    if(dizi[i][1]!="Şubat"):
         sum=sum+dizi[i][2]
         count +=1
print("Tüm yılların Ocak - Mart Ortalaması: ",sum/count)

# Cevap 4

sum21=0 
count21=0
sum20=0 
sum22=0
count20=0
count22=0

for i in range(len(dizi)):
    if(dizi[i][1]!="Şubat"):
         if(dizi[i][0]==2020):
             sum20=sum20+dizi[i][2]
             count20 +=1
         elif(dizi[i][0]==2022):
             sum22=sum22+dizi[i][2]
             count22 +=1
         else:
             sum21=sum21+dizi[i][2]
             count21 +=1             
print("2020 yılı Ocak-Mart ortalaması",sum20/count20)
print("2021 yılı Ocak-Mart ortalaması",sum21/count21)
print("2022 yılı Ocak-Mart ortalaması",sum22/count22)             
         
   