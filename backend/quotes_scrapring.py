import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}

res = requests.get(url, headers=headers)

if res.status_code == 200:
    print(res.status_code)
    # lakukan sesuatu
    soup = BeautifulSoup(res.text, 'html.parser')

    f = open('temp/res.html', 'w', encoding='utf-8')
    f.write(res.text)
    f.close()

    with open('temp/res.html') as files:
        html = files.read()
        if html == "A woman is like a tea bag":
            pass
        else:
            pass


    # proses scraping
    header_content = soup.find('div', attrs={'class': 'col-md-8'})
    contents = header_content.find_all('div', attrs={'class':'quote'})
    for content in contents:
        pass
    
else:
    print(res.status_code)

