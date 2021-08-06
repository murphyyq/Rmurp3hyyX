import asyncio
import aiohttp
from aiohttp import ClientSession
import time
import socket
from aiohttp import connector
from aiohttp.http import RESPONSES

from aiohttp.streams import AsyncStreamIterator
# murphyy admin panel bulma aracı  murphyy tarafından yazıldı iyi çalışmalar dostum
print("""\33[91;1m  
murphyy admin panel arayan araç versiyon 001                              
      """)
target = input("/33[92;1mHEDEF URL'Yİ BURAYA GİR DOSTUM: /33[1;0m")
print("")
#Temel giriş filtresi
target = target.replace('https://','')
target = target.replace('http://','')
tar_list = target.split('/')
for tar in tar_list:
    if tar == '':
        tar_list.remove(tar)
target = '/'.join(tar_list)
target = 'http://' + target 
#Değiikenleri, işlevleri vb tanımlayın

start = time.time()
yay = []
conn = aiohttp.TCPConnector(
    family=socket.AF_INET,
    verify_ssl=False
)#bazılarının AsyncResolver ile yaşayabileceği sorunlar nedeniyle kullanıldı
async def fetch(url,session):
    async with session.get(url) as response:
        status = response.status #sayfanın açık olup olmadığını görmek için durum kodlarını alır
        if status == 200:
            print("\33[97;1mpew 👉😎👉 \33[1;0m{]\33[97;1m 👈😎👈 {}".format(response.url, status))
            yay.append(response.url)
        elif status == 404:
            print("\33[91;1m⚠️ \33[94;1m{}\33[91;1m ⚠️{}".format(response.url, status))
        elif status == 403:
            print("\33[91;1m⚠️ \33[94;1m{}\33[91;1m ⚠️ \33[95;1m{}")
        else:
            print("\33[95;1m??? {} ??? {}".format(response.url, status))
        return await response.read()
    
async def run():
        url = target + "{}"
        tasks = []
        admin_list = open('admin.txt', 'r')
        paths = []
        for path in admin_list:
            path = path.replace('\n','')
            paths.append(path)
            
        async with ClientSession(connector=conn) as session: #görevleri oluşturur
            for i in paths:
                task = asyncio.ensure_future(fetch(url.format(i), session))
                tasks.append(task)
                
            responses = asyncio.gather(*tasks)
            await responses
 #döngü başlat
loop = asyncio.get_event_loop()           
 
future = asyncio.ensure_future(run())
loop.run_until_complete(future)
 
#sonuçlar
end = time.time()
script_time = end - start
print("\33[93;1mTarama alındı {} tamamlamak için saniye\n".format(script_time))
print("\33[91;1m### \33[93;1mSonuçlar \33[91;1m###\33[1;0m")
if len(yay) == 0:
     print("\33[94;1m!!! Paneli Bulamadım dostum (sad🥺)")
else:
    for y in yay:
        print(y)
print("\33[91;1m###########")
                



