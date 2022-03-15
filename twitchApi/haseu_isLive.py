import requests
import json
from _protectedInfo import GETTING_ACCESS_TOKEN_URL
from _protectedInfo import GETTING_STREAMER_STATUS_URL
from _protectedInfo import STREAMER_ID
from _protectedInfo import STREAMER_NAME
from _protectedInfo import MY_CLIENT_ID
from _protectedInfo import KAKAO_REQUEST_URL
from _protectedInfo import HASEU_TWITCH_URL
from templateObject import template_object
from templateObject import ONPic
from templateObject import OFFPic


def getAccessTokenForTwitch():
    response = requests.post(GETTING_ACCESS_TOKEN_URL)
    return response.json().get('access_token')


def makeHeaders(access_token):
    return {
        'Authorization' : 'Bearer ' + access_token,
        'client-id' : MY_CLIENT_ID
    }


def getStreamersNameWithStreamerId():
    token = getAccessTokenForTwitch()
    headers = makeHeaders(token)
    response = requests.get(GETTING_STREAMER_STATUS_URL, headers=headers)

    return response.json().get('data') # streamer list who have same STREAMER_ID


def getTwitchStreamerInfo(): 
    HASEU = dict()
    streamers = getStreamersNameWithStreamerId()
    for streamer in streamers:
        if streamer.get('broadcaster_login') == STREAMER_ID:
            HASEU = streamer
            break
    
    return HASEU


# print(getTwitchStreamerInfo())
'''
{'broadcaster_language': 'ko', 'broadcaster_login': 'haseu_', 
'display_name': '하세유', 'game_id': '509658', 'game_name': 'Just Chatting', 
'id': '700284891', 'is_live': False, 'tag_ids': [], 
'thumbnail_url': 'https://static-cdn.jtvnw.net/jtv_user_pictures/e6028012-f6fa-4000-88e7-a18623e30580-profile_image-300x300.png', 
'title': '월욜일 ٩(๑❛ᴗ❛๑)۶💕', 'started_at': ''}
'''


def getKakaoAccessToken():
    with open("kakao_code.json", "r") as fp:
        return json.load(fp).get('access_token')


def makeKakaoRequestHeader(access_token):
    return {
        "Content-Type" : "application/x-www-form-urlencoded",
        "Authorization" : "Bearer " + access_token
    }


# def makeMessage(myMessage):
#     return {
#         "template_object" : json.dumps({
#             "object_type" : "text",
#             "text" : myMessage,
#             "link" : {
#                 "web_url" : HASEU_TWITCH_URL,
#                 "mobile_web_url" : HASEU_TWITCH_URL
#             },
#             "button_title" : "Go!"
#         })
#     }

def makeMessage(myMessage, isLive):
    return {
        "template_object" : json.dumps({
            "object_type": "feed",
            "content": {
                "title": STREAMER_NAME + "님 방송알림 ><",
                "description": myMessage,
                "image_url": ONPic if isLive else OFFPic,
                "image_width": 20,
                "image_height": 20,
                "link": {
                    "web_url": "http://www.daum.net",
                    "mobile_web_url": "http://m.daum.net",
                    "android_execution_params": "contentId=100",
                    "ios_execution_params": "contentId=100"
                }
            }
        })
    }


def sendMessage(myMessage, isLive):
    token = getKakaoAccessToken()
    headers = makeKakaoRequestHeader(token)
    data = makeMessage(myMessage, isLive)
    response = requests.post(KAKAO_REQUEST_URL, headers=headers, data=data)
    response.status_code


def main():
    streamerInfo = getTwitchStreamerInfo()
    status = True
    # status = streamerInfo.get('is_live')
    description = '방송키셨다ㅏㅏㅏㅏㅏ!!' if status else streamerInfo.get('display_name') + "님은 자는 중 ㅜ"
    sendMessage("현재 " + streamerInfo.get('display_name') + "님 방송상태는? → " + description, status)


if __name__ == "__main__":
    main()

