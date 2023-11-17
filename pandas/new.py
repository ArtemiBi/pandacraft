import pandas as pd

df = pd.read_csv("GooglePlayStore_wild.csv")

df["Rating"].fillna(-1, inplace=True)

df.dropna(inplace=True)



def make_price(price):
    if price[0] == "$":
        return float(price[1:])
    return 0 

df["Price"] = df["Price"].apply(make_price)

def make_size(size):
    if size[-1] == "M":
        return float(size[:-1])
    elif size[-1] == "k":
        return float(size[:-1])/1024
    
    return -1

df["Size"] = df["Size"].apply(make_size)

#print(df.info())


#print(df.Henres.tail(20))

def split_genres(genres):
    return genres.split(";")

df["Genres"]= df["Genres"].apply(split_genres)
#print(df.Genres.head())

df["Number of Genres"] = df["Genres"].apply(len)
#print(df[["Genres", "Number of Genres"]].head(20))


def make_installs(installs:str):
    installs = installs.replace(",","")
    if installs[-1] == "+":
        return int(installs[:-1])
    return installs

df["Installs"] = df["Installs"].apply(make_installs)

avg = df.groupby(by = 'Number of Genres').Installs.mean()
print(avg)