
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

Companies = []
def get_name_purpose():
    web_site = requests.get("http://18.206.38.144:8000/random_company")
    soup = BeautifulSoup(web_site.text, features="html.parser")
    get_name = soup.find("li", string=re.compile("Name")).text[6:]
    get_purpose = soup.find("li", string=re.compile("Purpose")).text[9:]
    Companies.append((get_name,get_purpose))

for i in range(50):
    get_name_purpose()
    i += 1

df_Companies = pd.DataFrame(Companies)
df_Companies.columns = ['Name','Purpose']
print(df_Companies)
