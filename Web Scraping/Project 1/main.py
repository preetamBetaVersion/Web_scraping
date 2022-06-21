from bs4 import BeautifulSoup
with open('index.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    links = soup.find_all('div', attrs={'class':'protect'})
    for link in links:
        website_name = link.a.text
        print(f'{website_name} : use this link to reach the homepage')