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

plt.figure(figsize=(20, 20))
plt.scatter(df.Weight,df.CO2,s=df.Weight//10,c=np.log10(df.Volume),alpha=0.7)
plt.colorbar(label="Motor Volume", orientation="vertical")
plt.xlabel('Weight',color='g',size=14)
plt.ylabel('CO2',color='r',size=14)
plt.title('Assignment-31')

plt.show()

