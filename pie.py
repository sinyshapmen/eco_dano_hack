import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('final.csv')

industry_counts = df['отрасль'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(industry_counts, labels=industry_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Распределение отраслей')
plt.axis('equal') 
plt.tight_layout()
plt.savefig('otrasl.png')
plt.show()
