# Projeto Visualisação da Informação
Nome: Felipe Rego Sacchi

Instituição: Cruzeiro do Sul Virtual

Curso: CIÊNCIA DA COMPUTAÇÃO

Link do dataset utilizado (dever ser apenas 1 e estar disponível na internet):

https://www.kaggle.com/datasets/azminetoushikwasi/-lionel-messi-all-club-goals?resource=download

Link do meu video de apresentação:

https://www.loom.com/share/6ac65a9d2f714937a5a8ba94688e57cd

## Plot 1

🔷Breve descrição (Análise dos dados)

Primeiro gráfico acabei utilizando a técnica de Barras para conseguir demonstrar a quantidade total de gols
em que o Lionel Messi fez por temporada.
Então podemos notar no eixo Y a quantidade de gols e no eixo X as temporadas. Deixei na ordem
decrescente de numero de gols

🔷Código fonte
```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

tabela = pd.read_csv("DataSet/data.csv")

count = tabela["Season"].value_counts().values
season = tabela["Season"].value_counts().index

plt.figure(figsize=(10, 8))
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

```
![alt text](https://github.com/felipesacchi/projeto_visualizazao_da_informacao/blob/master/Imagens/plot1.png)

## Plot 2

🔷Breve descrição (Análise dos dados) 

Segundo gráfico escolhido foi o de setor para demonstrar a porcentagem de gols Dentro de Casa (“Home”) e Fora de Casa (“Away”) na carreira de Leonel Messi.

🔷Código fonte
```python
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
```

<p align="center">
  <img src="https://github.com/felipesacchi/projeto_visualizazao_da_informacao/blob/master/Imagens/plot2.png">
</p>


## Plot 3

🔷Breve descrição (Análise dos dados) 

Terceiro gráfico, escolhi duas técnicas em conjunto para formar uma linha com pontos (plot, scatter).

Nesse gráfico eu mostro a quantidades de Gols nos times oponentes que sofreram mais de 15 gols na carreira do Lionel Messi

🔷Código fonte
```python
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

plt.grid(alpha=.2)
plt.show()
```
<p align="center">
  <img src="https://github.com/felipesacchi/projeto_visualizazao_da_informacao/blob/master/Imagens/plot3.png">
</p>
