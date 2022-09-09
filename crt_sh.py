import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", help = "enter your domain")
parser.add_argument("-a", "--alive", action='store_true' , help = "display only alive domains")
args=parser.parse_args()

domain =args.domain
query = {'q': domain}
req = requests.get('https://crt.sh/?', params=query)
soup = BeautifulSoup(req.text,features="html.parser")

table = soup.find_all("table")[2]
html_td = table.find_all("td")

rows = []
for i in html_td:
    rows.append(i.text)
rows = np.asarray(rows)
rows = np.split(rows, len(rows)/7)

df = pd.DataFrame(rows, columns = ['crt.sh ID','Logged At','Not Before','Not After','Common Name','Matching Identities','Issuer Name'])

df = df.drop_duplicates(subset=['Common Name'])

num_df=df['Common Name'].to_numpy().tolist()

if args.alive==True:
    for x in num_df:
        try:
            r = requests.get("https://"+x,timeout=2)
            print(x)
        except requests.exceptions.RequestException as e:
            continue
else:
    print((df['Common Name'].to_csv(index=False, header=False)))
