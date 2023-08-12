import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\Ariya Rayaneh\Desktop\data.csv")

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

n = 100
xs=df['Volume']
ys = df['Weight']
zs = df['CO2']

ax.scatter(xs, ys, zs,c=df['Weight'],s=df['Volume']//20,alpha=0.5)

ax.set_xlabel('Motor Weight')
ax.set_ylabel('Motor Volume')
ax.set_zlabel('CO2')

plt.show()