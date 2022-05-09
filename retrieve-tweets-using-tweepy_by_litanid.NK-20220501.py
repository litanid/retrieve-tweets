from datetime import datetime,timezone,timedelta
import sys
import tweepy
import re
import os
import json

'''
retrieve-tweets-using-tweepy_by_litanid.HK-20220501.py

Site: https://github.com/litanid/retrieve-tweets


命令运行方法：
python3 retrieve-tweets-using-tweepy_by_litanid.HK-20220501.py 20220101 20220430
前一个时间为起始时间，从当天0点0分0秒开始，后一个为结束时间，当天的23点59分59秒止
运行成功后，会在运行目录生成20220101-20220430.js文件，再用
python3 extract-tweets-to-hugomd_by_litanid_after_20220501.py 20220101-20220430.js
'''

beginday = sys.argv[1]
endday = sys.argv[2]
beginday_datetime_string = beginday + " 00:00:00"  #起始日期当天的0点0分0秒
endday_datetime_string = endday + " 23:59:59"  #结束日期为当天的23点59分59秒
outputFile_name0 = beginday + "-" + endday  #输出文件名
outputFile_name1 = ".js"  #输出文件扩展名
outputFile_name = outputFile_name0 + outputFile_name1

#转换成datetime类型
beginday_datetime = datetime.strptime(beginday_datetime_string,'%Y%m%d %H:%M:%S')
endday_datetime = datetime.strptime(endday_datetime_string,'%Y%m%d %H:%M:%S')

#北京时间转换成格林尼治时间UTC
beginday_datetime_beijing = beginday_datetime.replace(tzinfo=timezone(timedelta(hours=8))) #输入时间确定为北京时间
endday_datetime_beijing = endday_datetime.replace(tzinfo=timezone(timedelta(hours=8))) #输入时间确定为北京时间
beginday_datetime_utc = beginday_datetime_beijing.astimezone(timezone.utc) #转换为utc时间
endday_datetime_utc = endday_datetime_beijing.astimezone(timezone.utc) #转换为utc时间
beginday_datetime_utc = beginday_datetime_utc.replace(tzinfo=None) #时间转换成为offset-naive才能进行比较
endday_datetime_utc = endday_datetime_utc.replace(tzinfo=None) #时间转换成为offset-naive才能进行比较

consumer_key = 'CBhSiD8h'
consumer_secret = 'zlUr3JyrPzMFQLNCo7hLCzG'
access_token = '1448870LJibBcAQOSZP'
access_secret = 'xvsyCFjItYp28RI2RufWB'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
#如果被墙，可以采用代理  auth_api = API(auth,proxy="127.0.0.1:1080")

tweets = []
for tweet in tweepy.Cursor(api.user_timeline,tweet_mode="extended").items():
	'''
			Cursor(auth_api.user_timeline, id=target)其他一些参数 
			screen_name = screen_name,count=200, tweet_mode="extended"
			Instead of full_text=True you need tweet_mode="extended"
			Then, instead of text you should use full_text to get the full tweet text.
			tweets = [[tweet.full_text] for tweet in new_tweets]

			tweets = []
		    for tweet in tweepy.Cursor(api.user_timeline,
		                       screen_name=<twitter_handle>,
		                       since_id = <since_id>
		                       ).items(<count>):
		        tweets.append(tweet)
	'''
	if tweet.created_at >= beginday_datetime_utc and tweet.created_at <= endday_datetime_utc :
		tweets.append(tweet._json)

with open(outputFile_name,'w') as outputFile:
		print("Grailbird.data.tweets_{0} =".format(outputFile_name0),file = outputFile)
		tweets_output = json.dumps(tweets, sort_keys=True, indent=4, separators=(',', ':'))
		tweets_output = re.sub('"full_text":"','"text":"',tweets_output)  #获取tweet推文全部内容
		print(tweets_output,file = outputFile)   
		#格式化输出json字符串

