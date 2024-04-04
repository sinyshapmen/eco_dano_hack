import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('final.csv', decimal=',')
df = df[df['эко_индекс'] != 1.0]

value_counts = df['b2b/b2c'].value_counts()

plt.bar(value_counts.index, value_counts.values)
plt.xlabel('')
plt.ylabel('кол-во')
plt.title('b2b/b2c')

plt.tight_layout()
plt.savefig('tyyy.png')
plt.show()