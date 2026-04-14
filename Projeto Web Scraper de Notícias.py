import requests

url = "https://g1.globo.com" 
resposta = requests.get(url) 

print(resposta.status_code) 
print(resposta.text[:500])


from bs4 import BeautifulSoup

soup = BeautifulSoup(resposta.text, "html.parser") 

manchetes = soup.find_all("a", class_="feed-post-link") 
for m in manchetes[:5]: 
    titulo = m.get_text(strip=True)
    link = m["href"] 

    print("Título:", titulo)
    print("Link:", link) 
    print("-" * 40) 


import csv

with open("notícias.csv", "w",newline="",encoding="utf-8") as f:
    writer = csv.writer(f) 
    writer.writerow(["Manchete"])

    for m in manchetes:
        writer.writerow([m.text.strip()]) 



import schedule
import time

schedule.every(1).hours.do(lambda: print("Executando o scraper..."))

while True:
    schedule.run_pending() 
    time.sleep(1) 
