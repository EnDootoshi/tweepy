#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Tweepyのインポート
import tweepy
import config

#keyの取得
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
AS = config.ACCESS_SECRET
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

api = tweepy.API(auth)

api.update_status("tweepyでのツイートです！！")

