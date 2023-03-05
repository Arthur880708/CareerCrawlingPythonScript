"""
Nexon Career 스펙 파싱
* 규격이 모두 달라서 어떻게 쓸지 이후에 고민해야 할 듯. *
"""

import requests
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

# Send a GET request to the website you want to scrape
base_url = 'https://career.nexon.com'
href = '/user/recruit/member/postList?joinCorp=NX&jobGroupCd=5&reSubj='
url = urljoin(base_url, href)
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all div elements with class "wrapPostGroup"
#wrap_post_groups = soup.find_all('div', class_='wrapPostGroup')
wrap_post_groups = soup.find_all("div", {"class": "wrapPostGroup"})

# Loop through the wrapPostGroup elements and extract the information you need
for wrap_post_group in wrap_post_groups:
    # Find all post titles within the current wrapPostGroup element
    post_titles = wrap_post_group.find_all('a', class_='postListItem')
    for post_title in post_titles:
        # Find the post address within the current post title element
        href = post_title['href']
        href = re.sub(r'\u00a4tPage=0', '', href)
        url = urljoin(base_url, href)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        span = soup.find('div', {'class': 'detailContents'}).text.strip()
        if span is not None:
            print(f'Span text: {span}')
        else:
            print('Span not found')
        print('-' * 50)