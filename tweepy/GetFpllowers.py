#coding:utf-8

from requests_oauthlib import OAuth1Session
import json
import config

# キーをセット
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
AS = config.ACCESS_SECRET

# OAuth処理
twitter = OAuth1Session(CK, CS, AT, AS)

url = "https://api.twitter.com/1.1/followers/list.json" #タイムライン取得エンドポイント

params ={'count' : 10} #取得数
res = twitter.get(url, params = params)

if res.status_code == 200: #正常通信出来た場合
    followers = json.loads(res.text) #レスポンスからフォロワーリストを取得
    users_info=followers['users']   #usersに各ユーザーの情報が配列として格納されている
    for user_info in users_info:    #配列から各要素を取り出し、user_infoに格納
        #json形式のファイルから値を取得
        print('ユーザー名:' + str(user_info['name']))
        print('フォロー数:' + str(user_info['friends_count']))
        print('フォロワー数:' + str(user_info['followers_count']))
        print('################################')
else: #正常通信出来なかった場合
    print("Failed: %d" % res.status_code)
