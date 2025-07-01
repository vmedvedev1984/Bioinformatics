import wget
#import ssl
import requests
from bs4 import BeautifulSoup

for i in range(12000, 20000):
    print(i)
    url = f'https://www.addgene.org/{i}/sequences/'
    page = requests.get(url)
    if page.status_code == 200:
        
        plasmid_name = []
        soup = BeautifulSoup(page.text, "html.parser")
        try:
            # Code that might raise an exception
            plasmid_name = repr(soup.find_all('span', class_='material-name')[0].string)  # This will raise a ZeroDivisionError
        except IndexError:
            # Code to execute if ExceptionType occurs in the try block
            print("КРИТИЧЕСКАЯ ОШИБКА В")
            print(soup.find_all('span', class_='material-name'))
            continue
        
        try:
            # Code that might raise an exception
            links = soup.find_all('a', class_='genbank-file-download')[0].get('href')  # This will raise a ZeroDivisionError
        except IndexError:
            # Code to execute if ExceptionType occurs in the try block
            print("Ошибка в " + plasmid_name)
            continue
        #links = soup.find_all('a', class_='genbank-file-download')[0].get('href')
        print(i)
        print(plasmid_name)
        plasmid_name = plasmid_name.replace("/", '_').replace(":", '_').replace("'","_").replace('"',"")
        r = requests.get(links)
        with open(f'D:\\plasmid\\{plasmid_name}.gbk', "wb") as file:
            file.write(r.content)
        
'''
url = 'https://www.addgene.org/54506/sequences/'


print(soup)
page = requests.get(url)
print(page.status_code)
plasmid_name = []
seqences = []
soup = BeautifulSoup(page.text, "html.parser")
#print(soup)
plasmid_name = repr(soup.find_all('span', class_='material-name')[0].string)
links = soup.find_all('a', class_='genbank-file-download')[0].get('href')
#current_link = soup.find_all().get('href')
print(plasmid_name)
print(links)

r = requests.get(links)
with open(f'D:\\plasmid\\{plasmid_name}.gbk', "wb") as file:
    file.write(r.content)
'''
#wget.download('https://media.addgene.org/snapgene-media/v3.0.0/sequences/393242/e51691b8-d669-40be-9df7-60f59e5d84f5/addgene-plasmid-54506-sequence-393242.gbk', out = "D:\\plasmid\\")