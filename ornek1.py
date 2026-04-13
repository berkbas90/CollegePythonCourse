import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

dosya=pd.read_excel("veri.xlsx")

ilgilikolonlar=dosya[["BirinciCeyrek","IkinciCeyrek","UcuncuCeyrek","DorduncuCeyrek"]].astype(float)

plt.boxplot(ilgilikolonlar)

plt.show()


