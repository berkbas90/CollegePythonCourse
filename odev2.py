dizi = [ [2020,"Ocak",300],[2020,"Şubat",500],[2020,"Mart",250],
         [2021,"Ocak",380],[2021,"Şubat",470],[2021,"Mart",350],
         [2022,"Ocak",350],[2022,"Şubat",450],[2022,"Mart",750]  
       ]

# Cevap 1
tmp = []
indice=0
for i in range(len(dizi)):
    tmp.append(dizi[i][2])

tmp.sort()

print(tmp)

for j in range(len(dizi)):
    if(dizi[j][2]==tmp[0]):
        indice=j
        break

print(f"En küçük değere sahip olan {dizi[indice]}")

# Cevap 2
sum=0
for b in range(len(dizi)):
    sum=sum+(dizi[b][2])
print("Aritmetik Ortalama",sum/len(dizi))

# Cevap 3

sum=0
#print(dizi[0][2],dizi[2][2],dizi[3][2],dizi[5][2],dizi[6][2],dizi[8][2])
count=0
for i in range(len(dizi)):
    if(i%5==0 or i==2 or i%3==0 or i==8):
         sum=sum+dizi[i][2]
         count +=1
print("Tüm yılların Ocak - Mart Ortalaması: ",sum/count)