import matplotlib.pyplot as plt
import pandas as pd

tabela = pd.read_csv("DataSet/data.csv")

plt.figure(figsize=(10, 8))
plt.title('Goals per venue', fontsize=30)

tabela.Venue.value_counts().plot(kind='pie',
                                 labels=['Home', 'Away'],
                                 wedgeprops=dict(width=.7),
                                 autopct='%0.2f%%',
                                 textprops={'fontsize': 15}
                                 )

plt.show()