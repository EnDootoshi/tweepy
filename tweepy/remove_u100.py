# Tweepyライブラリをインポート
import tweepy
import config

# 各種キーをセット
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_SECRET

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

#APIインスタンスを作成
api = tweepy.API(auth)
userid = "EnDoo_py" #自分のuserID

followers_id = api.followers_ids(userid) #自分のアカウントのフォロワーをすべて取得する
following_id = api.friends_ids(userid) #自分のアカウントのフォロイングをすべて取得する
for following in following_id: #自分がフォローしているユーザーだけ取得する
    if following not in followers_id: #自分のフォローしているユーザーで、フォロワーに属さなユーザーを取得する
        userfollowers = api.get_user(following).followers_count
        if userfollowers < 70:
            print("リムーブするユーザー名")
            username = api.get_user(following).name
            print(username)
            print("フォロワー数")
            print(userfollowers)
            api.destroy_friendship(following)
