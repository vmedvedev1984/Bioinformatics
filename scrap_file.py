import subprocess
import wget
import ssl
import requests

for i in range(10000, 40000):
    print(i)
    url = f'https://raw.githubusercontent.com/SciCrunch/RRID-Instruments/main/PDF/SCR_0{i}.pdf'
    if requests.get(url).status_code == 200:
        #url = f'https://raw.githubusercontent.com/SciCrunch/RRID-Instruments/main/PDF/SCR_0{i}.pdf'
        filename = wget.download(url, out = "D:\\Manual\\")
        print(f"Downloaded: {filename}")

