import requests
import config, json
from requests_oauthlib import OAuth1Session

#取得したkeyを以下で定義する
access_token = config.ACCESS_TOKEN
access_token_secret = config.ACCESS_SECRET
consumer_key = config.CONSUMER_KEY
consumer_key_secret = config.CONSUMER_SECRET


# タイムライン取得用のURL
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

#パラメータの定義
params = {'screen_name':'EnDoo_py',
          'exclude_replies':True,
          'include_rts':False,
          'count':200}

#APIの認証
twitter = OAuth1Session(consumer_key, consumer_key_secret, access_token, access_token_secret)

#リクエストを投げる
res = twitter.get(url, params = params)

f_out = open('./wordcloud.txt','w')

for j in range(100):
    res = twitter.get(url, params = params)

    if res.status_code == 200:

        # API残り
        limit = res.headers['x-rate-limit-remaining']
        print ("API remain: " + limit)
        if limit == 1:
            sleep(60*15)

        n = 0
        timeline = json.loads(res.text)
        # 各ツイートの本文を表示
        for i in range(len(timeline)):
            if i != len(timeline)-1:
                f_out.write(timeline[i]['text'] + '\n')
            else:
                f_out.write(timeline[i]['text'] + '\n')
#一番最後のツイートIDをパラメータmax_idに追加
                params['max_id'] = timeline[i]['id']-1

f_out.close()
