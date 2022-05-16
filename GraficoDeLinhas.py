import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

tabela = pd.read_csv("DataSet/data.csv")

plt.figure(figsize=(4, 5))
plt.subplot(211)

opponents = tabela.groupby('Opponent').size().reset_index(name='count')
fav_opponents = opponents[opponents["count"] > 15]

plt.plot(fav_opponents['Opponent'], fav_opponents['count'], color="Blue")
plt.scatter(fav_opponents['Opponent'], fav_opponents['count'], color="Black")

plt.xticks(fontsize=10, rotation='vertical')
plt.yticks(np.arange(15, 40, 2))
plt.xlabel("Opponents", fontsize=15)
plt.ylabel("Goals", fontsize=15)
plt.title("Favourite Opponents", fontsize=20)

plt.grid(alpha=.1)
plt.show()