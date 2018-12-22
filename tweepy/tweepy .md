
# エラーについて

```python
tweepy.error.TweepError: [{'code': 32, 'message': 'Could not authenticate you.'}]
```
アクセストークンをコピペするときにスペースが入ってしまったとか、API Keyを再生成したりするとうまくいくのですが、それに気づくのにずいぶんな時間を費やしてしまったりします･･･。あとはコンマ「,」のエンコードの問題だとか、さまざまな理由があげられています。

現在は「Twitter Developers」[text](https://dev.twitter.com/)にログイン後、自分のアイコンから「My Applications」から、任意のアプリケーションを選択。
画面右上の「Test Auth」押下です。

# Python3.7.0でtweepyを使おうとしたところ

Twitter Streaming APIをPython3.7.0環境のTweepy使おうとしたところ、次のようなエラーが出た。

```python
 python main.py
Traceback (most recent call last):
  File "main.py", line 7, in <module>
    import tweepy
  File "/home/ubuntu/.venv/watson/lib/python3.7/site-packages/tweepy/__init__.py", line 17, in <module>
    from tweepy.streaming import Stream, StreamListener
  File "/home/ubuntu/.venv/watson/lib/python3.7/site-packages/tweepy/streaming.py", line 358
    def _start(self, async):
                         ^
SyntaxError: invalid syntax
```

何かなーと思ったら、**async** が3.7.0から予約語に入っていた。

What’s New In Python 3.7

## 対処方法

../site-packages/tweepy/streaming.py の async を sync などの変数名に置換してしまうこと
