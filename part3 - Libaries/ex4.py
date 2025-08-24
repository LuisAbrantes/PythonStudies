import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

data = {
    "Product": ["iPhone", "Macbook Pro", "AirPods"],
    "Price": [5000, 20000, 2000],
    "Storage": [50, 20, 30]
}

dfProducts = pd.DataFrame(data)

sns.scatterplot(x='Product', y='Storage', data=dfProducts)

plt.title('Storage per Product')

plt.show() 