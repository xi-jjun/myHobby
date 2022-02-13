
import json
import requests

auth_url = "https://kauth.kakao.com/oauth/authorize?client_id={TOJKEN}response_type=code"

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# 사용자 토큰
headers = {
    "Authorization": "Bearer " + "ACCESS_TOKEN"
}

template = {
    "object_type" : "list",
    "header_title" : "Kakao API TEST message",
    "header_link" : {
        "web_url" : "https://edu.ssafy.com/edu/board/notice/list.do",
        "mobile_web_url" : "https://edu.ssafy.com/edu/board/notice/list.do"
    },
    "contents" : [
        {
            "title" : "1. Edu.ssafy kakao message Test",
            "description" : "description test",
            "image_url" : "https://edu.ssafy.com/asset/images/header-logo.jpg",
            "image_width" : 50, "image_height" : 50,
            "link" : {
                "web_url" : "https://edu.ssafy.com/edu/board/notice/list.do",
                "mobile_web_url" : "https://edu.ssafy.com/edu/board/notice/list.do"
            }
        },
        {
            "title" : "2. 김재준 Github Blog 홍보",
            "description" : "많이 봐주세요ㅜ",
            "image_url" : "https://www.clipartmax.com/png/middle/319-3192667_sikkim-blog-transparent-background-typewriter-icon.png",
            "image_width" : 50, "image_height" : 50,
            "link" : {
                "web_url" : "https://xi-jjun.github.io/",
                "mobile_web_url" : "https://xi-jjun.github.io/"
            }
        }
        
    ],
    "buttons" : [
        {
            "title" : "웹으로 이동",
            "link" : {
                "web_url" : "https://edu.ssafy.com/edu/board/notice/list.do",
                "mobile_web_url" : "https://edu.ssafy.com/edu/board/notice/list.do"
            }
        }
    ]
    
}

data = {
    "template_object" : json.dumps(template)
}

res = requests.post(url, data=data, headers=headers)
print(res.status_code)
if res.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(res.json()))
