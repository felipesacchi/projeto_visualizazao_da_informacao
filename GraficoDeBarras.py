import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

tabela = pd.read_csv("DataSet/data.csv")

count = tabela["Season"].value_counts().values
season = tabela["Season"].value_counts().index

plt.figure(figsize=(5, 4))
color = []

goals = plt.bar(season, count, ec="k", alpha=1, color=sns.color_palette('tab20'))

for i in goals:
    h = i.get_height()
    plt.annotate('{}'.format(h),
                 xy=(i.get_x()+i.get_width()/2, h),
                 xytext=(0, 3),
                 textcoords='offset points',
                 ha='center'
    )

plt.xticks(fontsize=15, rotation='vertical')
plt.yticks(np.arange(0, 90, 10))
plt.xlabel("Season", fontsize=15)
plt.ylabel("Goals", fontsize=15)
plt.title("Goals per season", fontsize=30)

plt.grid(alpha=.1)
plt.show()
