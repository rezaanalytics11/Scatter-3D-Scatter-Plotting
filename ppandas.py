import numpy as np
import pandas
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
df = pandas.read_csv(r"C:\Users\Ariya Rayaneh\Desktop\data.csv")

print(df,5*'\n')

X=df[['Volume','Weight']]
Y=df.CO2
model=LinearRegression()
model.fit(X,Y)

y_predict=model.predict([[800,500]])

print(df.head(5))
print(y_predict)


dff=df.groupby('Car')['CO2'].max().reset_index()
dff=dff.sort_values(by="CO2")
plt.figure(figsize=(24,8))
sns.barplot(data=dff,x='Car',y='CO2')
plt.ylabel('CO2',fontsize=24,color='r')
plt.xlabel('Car',fontsize=24,color='g')
plt.show()


