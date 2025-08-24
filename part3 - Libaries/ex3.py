import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 


# Learning Pandas

data = {
    "Product": ["iPhone", "Macbook Pro", "AirPods"],
    "Price": [5000, 20000, 2000],
    "Storage": [50, 20, 30]
}

dfProducts = pd.DataFrame(data)

condition = dfProducts["Storage"]>25
scarceProd = dfProducts[condition]
dfProducts["totalValue"] = dfProducts["Storage"] * dfProducts["Price"]
dfProducts["productsDiscouted"] = dfProducts["Price"] * 0.9

print(dfProducts)
print(f"The products we have more than 15 are: \n {scarceProd}")


# Learning Seaborn

sns.barplot(x='Product', y='Storage', data=dfProducts)
plt.title('Storage per Product')
plt.show() 