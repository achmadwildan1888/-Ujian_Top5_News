print('Selamat datang, mau tahu berita apa hari ini?')
print('  [1] Berita seputar teknologi')
print('  [2] Berita seputar bisnis')
print('  [3] Berita seputar olahraga')
print('  [4] Berita seputar kesehatan')
print('  [5] Berita seputar science')

inputan= (input("Ketik pilihan Anda : " ))
api ='b8b12cc543944b87920bb96c250640b4'

import requests


if inputan=='1':
   for i in range (6):
        url1='https://newsapi.org/v2/top-headlines?country=id&category=technology&apiKey='+api
        data = requests.get(url1)
        listberita1 = data.json()
        for i in range(5):
                print(listberita1['articles'][i]['title'])
        break
if inputan=='2':
   for i in range (6):
        url2='https://newsapi.org/v2/top-headlines?country=id&category=business&apiKey='+api
        data2 = requests.get(url2)
        listberita2 = data2.json()
        for i in range(5):
                print(listberita2['articles'][i]['title'])
        break
if inputan=='3':
   for i in range (6):
        url3='https://newsapi.org/v2/top-headlines?country=id&category=sports&apiKey='+api
        data3 = requests.get(url3)
        listberita3 = data3.json()
        for i in range(5):
                print(listberita3['articles'][i]['title'])
        break
if inputan=='4':
   for i in range (6):
        url4='https://newsapi.org/v2/top-headlines?country=id&category=health&apiKey='+api
        data4 = requests.get(url4)
        listberita4 = data4.json()
        for i in range(5):
                print(listberita4['articles'][i]['title'])
        break
if inputan=='5':
   for i in range (6):
        url5='https://newsapi.org/v2/top-headlines?country=id&category=science&apiKey='+api
        data5 = requests.get(url5)
        listberita5 = data5.json()
        for i in range(5):
                print(listberita5['articles'][i]['title'])
        break
       
               
        
