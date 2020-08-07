import csv
import requests

def take_20_posts():

    token = "664921b4664921b4664921b40c663a7f8566649664921b4396437b5c6e3bf6e41a4e3b8"
    version = 5.122
    domain = 'nba'
    count = 10
    offset = 0
    all_posts = []
    while offset < 10:
        response = requests.get('https://api.vk.com/method/wall.get',
        params={
                'access_token': token,
                'v': version,
                'domain': domain,
                'count': count,
                'offset': offset
        })
        data = response.json()['response']['items']
        offset+=10
        all_posts.extend(data)

    return all_posts

def file_writer(data):
    with open('nba.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('likes','body','url'))
        for post in data:
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
            except:
                pass
            a_pen.writerow(post['likes']['count'],post['text'],img_url)



all_posts=take_20_posts()
file_writer(all_posts)