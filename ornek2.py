import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Arac": [
        "Renault Megane","Renault Megane","Renault Megane","Renault Megane","Renault Megane","Renault Megane","Renault Megane","Renault Megane","Renault Megane","Renault Megane","Renault Megane","Renault Megane",
        "Opel Astra","Opel Astra","Opel Astra","Opel Astra","Opel Astra","Opel Astra","Opel Astra","Opel Astra","Opel Astra","Opel Astra","Opel Astra","Opel Astra",
        "Honda Civic","Honda Civic","Honda Civic","Honda Civic","Honda Civic","Honda Civic","Honda Civic","Honda Civic","Honda Civic","Honda Civic","Honda Civic","Honda Civic"
    ],
    "Fiyat": [
        1000000,1050000,1100000,1250000,1275000,1300000,1350000,1400000,1640000,1700000,1740000,1810000,
        2100000,2300000,2450000,2500000,2550000,3000000,3300000,3350000,3400000,3650000,3900000,4100000,
        1500000,1650000,1900000,2050000,2100000,2150000,2200000,2200000,2250000,2275000,2300000,2500000
    ]
})

print(df.head(5))

plt.figure(figsize=(9,5))

sns.boxplot(
    x="Arac",
    y="Fiyat",
    data=df,
    palette="Set2"
)

plt.xticks(rotation=30)  
plt.title("Yılın 12 ayi icin C Segmenti Otomobil Fiyatları")

plt.show()