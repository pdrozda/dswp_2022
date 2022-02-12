import pandas as pd

url="https://stooq.pl/q/d/l/?s=agt&i=d"
c=pd.read_csv(url)
print(c.head())



url="https://stooq.pl/q/d/l/?s=agt&d1=20201108&d2=20220128&i=d"
c=pd.read_csv(url)
print(c.head())



url="https://stooq.pl/q/d/l/?s=bos&d1=20100203&d2=20220204&i=w"
c=pd.read_csv(url)
print(c.head())



def dane_spolek(spolki):
    for spolka in spolki:
        url = "https://stooq.pl/q/d/l/?s="+spolka+"&d1=20100203&d2=20220204&i=w"
        c = pd.read_csv(url)
        print(c.head())

tickery= ['bos','agt']
dane_spolek(tickery)