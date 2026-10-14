import requests
import pandas as pd


response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=10)
response.raise_for_status

users = response.json()

df = pd.json_normalize(users)

df = df[["id", "name", "email", "address.city", "company.name"]]
df = df.rename(columns = {"address.city":"city", "company.name":"company"})
print(df)

df.to_csv("users_clean.csv", index = False)
