import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(size=100)
sns.kdeplot(data, fill=True, color='green')

plt.title('Densidad')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()