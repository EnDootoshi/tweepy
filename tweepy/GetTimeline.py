#coding:utf-8
from requests_oauthlib import OAuth1Session
import json
import config
# Accesss Token Secert

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
AS = config.ACCESS_SECRET

twitter = OAuth1Session(CK, CS, AT, AS) #認証処理

url = "https://api.twitter.com/1.1/statuses/user_timeline.json" #タイムライン取得エンドポイント

params ={'count' : 5} #取得数
res = twitter.get(url, params = params)

if res.status_code == 200: #正常通信出来た場合
    timelines = json.loads(res.text) #レスポンスからタイムラインリストを取得
    for line in timelines: #タイムラインリストをループ処理
        #json形式のファイルから値を取得（※）
        print(line['user']['name']+'::'+line['text'])
        print(line['created_at'])
        print('##########################################')

else: #正常通信出来なかった場合
    print("Failed: %d" % res.status_code)
