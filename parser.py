# import requests,webbrowser
# from bs4 import BeautifulSoup
# token=[]
# url="https://vk.com/search?c%5Bcountry%5D=4&c%5Bname%5D=1&c%5Bper_page%5D=40&c%5Bsection%5D=people"
# user_agent='Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
# HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0', 'accept': '*/*'}
# def get_html(url,params=None):
#     html=requests.get(url, headers=HEADERS, params=params)
#     # print(html.text)
#     return html
# r=get_html(url)
# def parse_html(html):
#     soap=BeatifulSoup(html)
from part_one import *
import json
from auth_data import token
domains= open("domainlist.txt")
for domain in domains:
    wall=get_wall_posts(domain)
    # print(wall)
    posts=wall["response"]["items"]
    f=open(domain+".txt","w")
    for post in posts:
        # print(post.keys()[5])
        # repost=post['copy_history']
        text=post['text']
        f.write(text)
        
        # # copy_text=post['copy_history']
        # # text=text+"   "+ copy_text
        # print(type(copy_text))
        # print("---------------------------------------------------------------------------------------------------------------------------------------------")
        # print(text)