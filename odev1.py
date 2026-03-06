sifre =input("Şifreyi girin: ")
sifreoutput=""
basamak=0
halve1=""
halve2=""
for i in range(len(sifre)):
    basamak=int(sifre[i])
    basamak +=7
    basamak %=10
    sifreoutput=sifreoutput+str(basamak)
for j in range(len(sifreoutput)):
    if j==2:
        halve1=halve1+sifreoutput[j]
    elif j==0:
        halve1=halve1+sifreoutput[j]
    elif j==1:
        halve2=halve2+sifreoutput[j]
    else:
        halve2=halve2+sifreoutput[j]
print("Çıkan şifre: ",halve2+halve1)