import os
import json
import requests

from naverpay_notice_parser import get_notice_list

filePath = '/data.json'
webhookUrl = ''

oldArticles = []
currentArticles = get_notice_list()
if len(currentArticles) == 0:
    print('Current Atticles not found.')
    exit()

if os.path.exists(filePath):
    with open(filePath, 'r') as f:
        oldArticles = json.load(f)

        # 예전 데이터와 비교해서 동일하면 그냥 종료. 그런데 귀찮기도 하고 맨 위가 다르면 결국 다른 거니까 최상단에 하나만 비교해본다.
        if len(oldArticles) > 0 and oldArticles[0]["title"] == currentArticles[0]["title"] and oldArticles[0]["url"] == currentArticles[0]["url"]:
            exit()


isStop = False
newArticles = []
for currentArticle in currentArticles:
    for oldArticle in oldArticles:
        if oldArticles["title"] == currentArticles["title"] and oldArticles["url"] == currentArticles["url"]:
            isStop = True
            break
    if isStop:
        break
    newArticles.append(currentArticle)
if len(newArticles) == 0:
    exit()

content = {
    'content': '새로운 네이버페이 공지사항이 등록되었습니다.',
    'embeds': newArticles[:5]
}
headers = {
    'Content-Type': 'application/json'
}
response = requests.post(webhookUrl, data=json.dumps(content), headers=headers)
if response.status_code != 204:
    print("Cannot send a message : [{}] {}", response.status_code, response.content)
    exit()

with open(filePath, 'w') as f:
    json.dump(currentArticles, f)
