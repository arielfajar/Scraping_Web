#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://proxyway.com/reviews"  # Ganti dengan URL yang diinginkan

titles_list = []

# Looping untuk mengambil data dari 3 halaman
for page in range(1, 4):
    url = f"{base_url}/page/{page}"

    # Mengirim permintaan GET ke URL
    response = requests.get(url)

    # Membuat objek BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Menemukan semua elemen judul di halaman
    titles = soup.find_all("h3", class_="archive-list__title")  # Sesuaikan dengan kelas yang digunakan pada halaman

    # Menyimpan data judul ke dalam list
    for title in titles:
        titles_list.append(title.text)

# Menyimpan data ke dalam file CSV
filename = "title.csv"
with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title"])  # Menulis header kolom
    writer.writerows(zip(titles_list))  # Menulis data judul

print("Data judul telah berhasil disimpan ke dalam file CSV.")


# In[ ]:




