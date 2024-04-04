import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('final.csv', decimal=',')
df = df[df['эко_индекс'] != 1.0]

# разделение датасета на b2c и b2b
df_btc = df[df['b2b/b2c'] == 'b2c']
df_btb = df[df['b2b/b2c'] == 'b2b']

# создание боксплота по b2c/b2b
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

ticks = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
fhhf = sns.boxplot(y='эко_индекс', data=df_btc, ax=axes[0], orient='h')
axes[0].set_title('btc')
axes[0].set_ylabel('aa')
fhhf.set_yticks(ticks)
fhhf.set_yticklabels(ticks)
fhhf.set_ylim(axes[0].get_ylim())

two  = sns.boxplot(y='эко_индекс', data=df_btb, ax=axes[1], orient='h')
axes[1].set_title('btb')
axes[0].set_ylabel('эко_индекс')
two.set_yticks(ticks)
two.set_yticklabels(ticks)
fhhf.set_ylim(axes[0].get_ylim())


plt.tight_layout()

plt.savefig('filipp.png')

plt.show()

# разделение датасета на размеры компаний
df_small = df[df['размер'] == 'Малый']
df_median = df[df['размер'] == 'Средний']
df_big = df[df['размер'] == 'Крупный']

# создание боксплота по b2c/b2b
ticks = [0.0, 0.2, 0.4, 0.6, 0.8, 1]
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

one = sns.boxplot(y='эко_индекс', data=df_small, ax=axes[0], orient='h')
axes[0].set_title('small')
axes[0].set_ylabel('ecoindex')
one.set_yticks(ticks)
one.set_yticklabels(ticks)
one.set_ylim(axes[0].get_ylim())

two = sns.boxplot(y='эко_индекс', data=df_median, ax=axes[1], orient='h')
axes[1].set_title('normal')
axes[1].set_ylabel('ecoindex')
two.set_yticks(ticks)
two.set_yticklabels(ticks)
two.set_ylim(axes[0].get_ylim())

three = sns.boxplot(y='эко_индекс', data=df_big, ax=axes[2], orient='h')
axes[2].set_title('big')
axes[2].set_ylabel('ecoindex')
three.set_yticks(ticks)
three.set_yticklabels(ticks)
three.set_ylim(axes[0].get_ylim())

plt.tight_layout()
plt.savefig('size_box.png')
plt.show()


