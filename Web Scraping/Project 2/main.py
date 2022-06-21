from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://krishna.org/').text

soup  = BeautifulSoup(html_text, 'lxml')

posts = soup.find_all('article', attrs={'class':'omc-blog-two omc-half-width-category'})

for post in posts:
    post_header = post.find('h2').text
    post_date = post.find('p', attrs={'class':'omc-blog-two-date'}).text
    print(f'''
    Header : {post_header},
    post date and author : {post_date}
    ''')
    print('\n')
