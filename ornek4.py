import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

random_values = np.random.randint(0, 100, size=250)
cinsiyet = np.random.randint(1,3,size=250)


df = pd.DataFrame({
    "Ders Notu": random_values,
    "Cinsiyet": cinsiyet
})

df["Cinsiyet"] = df["Cinsiyet"].replace({1: "Erkek", 2: "Kadın"})

print(df.head(5))
plt.title("BEYB5145 Python ile Veri Analitiği Uygulamaları Dersi")
sns.boxplot(y=df["Cinsiyet"],x=df['Ders Notu'],color=".8", linecolor="#137", linewidth=.75)

plt.show()





