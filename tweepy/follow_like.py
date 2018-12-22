# -*- coding:utf-8 -*-

# Tweepyライブラリをインポート
import tweepy

# config.pyから各種キーを使うためインポート
import config

# キーをセット
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_SECRET

# OAuth処理
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)


#APIインスタンス作成
api = tweepy.API(auth)


# ここに検索キーワードを入れる
q = "SEARCH_WORDS"
# 取得数を設定
count = 200

# 検索結果
search_results = api.search(q=q, count=count)

for result in search_results:
    username = result.user._json['screen_name']
    # ツイートのstatusオブジェクトから、ツイートidを取得
    user_id = result.id
    print(user_id)
    # ツイートのstatusオブジェクトから、userオブジェクトを取り出し、名前を取得
    user = result.user.name
    print(user)
    tweet = result.text
    print(tweet)
    time = result.created_at
    print(time)
    try:
        api.create_favorite(user_id) #ファボる
        print(user)
        print("をいいねしました")
        api.create_friendship(user_id)
        print("をフォローしました")
    except:
        print("もうすでにいいねかフォローしてます")
    print("##################")
