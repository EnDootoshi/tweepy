# -*- coding:utf-8 -*-
import sys
import re
import pprint
import MeCab
import json, config
import collections
import warnings
from requests_oauthlib import OAuth1Session
from operator import itemgetter

warnings.filterwarnings('ignore')

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
AS = config.ACCESS_SECRET

twitter = OAuth1Session(CK, CS, AT, AS)

# 引数で指定されたユーザー名
args = sys.argv
twitter_name = args[1]

# 最新100件を取得
twitter_params ={'count' : 100}
# twitterの自分のページのURL
url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=" + twitter_name

res = twitter.get(url, params = twitter_params)

text = ""

if res.status_code == 200:
    timelines = json.loads(res.text)
    for line in timelines:
        # APIの結果から、ツイート内容だけ取り出す
        text += re.sub("https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", "", line['text']) + "\n"

    words = []
    m = MeCab.Tagger("-Ochasen")
    node = m.parseToNode(text)
    while node:
        # 意味のありそうな名詞だけを対象にして集計
        if node.feature.startswith("名詞,一般") or node.feature.startswith("名詞,固有名詞") or node.feature.startswith("名詞,形容動詞") or node.feature.startswith("名詞,サ変接続"):
          words.append(node.surface)
        node = node.next

    counter = collections.Counter(words)
    counter = sorted(counter.items(), key=itemgetter(1), reverse=True)

    i = 0
    print("＊＊＊＊ @" + twitter_name + "さんが最近のTweetでよく使った単語TOP10 ＊＊＊＊")
    for k, v in counter:
        print(k.encode('utf-8') + "・・・" + str(v) + "回")
        i = i + 1
        if i > 10:
          break

else:
    print("Failed: %d" % res.status_code)
