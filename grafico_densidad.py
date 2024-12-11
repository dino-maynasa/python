import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(size=1000)
sns.kdeplot(data, fill=True, color='blue')

plt.title('Densidad')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()