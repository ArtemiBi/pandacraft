import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("GoogleApps.csv")




#лінійний графік

#d = [5,7,3,10,11,15,20,1,0,2]

#s = pd.Series(data=d)

#s.plot()

#plt.show()

#гістограмва

#temp = df.Size
#temp.plot(kind="hist", bins=5)
#plt.show()

#Діаграма розсіювання

df.plot(kind="scatter", x="Rating", y="Installs")
plt.show()

