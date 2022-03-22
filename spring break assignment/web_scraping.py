from bs4 import BeautifulSoup
import requests

with open('raw_script_urls.txt') as f:
    lines = f.readlines()

urls = []
names = []
for line in lines:
    nlist = line.split(" +++$+++ ")
    urls.append(nlist[2].strip())
    names.append(nlist[1])

def scrape(url):
    response = requests.get(url)
    html_string = response.text
    return html_string

for i in range(len(urls)):
    towrite = scrape(urls[i])
    soup = BeautifulSoup(towrite, "html.parser")
    fname = names[i] + '.txt'
    with open(fname, 'w') as f:
        f.write(soup.text)
