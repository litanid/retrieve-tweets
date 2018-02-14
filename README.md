
用 `grailbird_update` 更新备份 Twitter 我的存档包（见 https://www.yiwan.pro/index.php/ltd_documents/384-use-grailbird_update-to-backup-tweets.html 文章和我的仓库 extract-tweets：
https://github.com/litanid/extract-tweets ），总是感觉不是那么可靠，毕竟获取 tweets 过程对自己是透明的，不能完全由自己掌握，而且`grailbird_update` 更新获取的 tweets 数据或多或少有那么点不足，如 tweet text 内容默认不显示全部，如果内容字数较多；还有 tweet 里本来就有图片，但获取的数据里没有包含；由于时间差的原因，获取的以年月命名的数据文件，有时下个月的数据保存在这个月里；诸如还有较多，暂不细述。我想要的是，给定时间段，就获取这个时间段内的 tweets 数据，text 内容全部显示，其他信息可能由于 twitter 的限制，不能获取那是没办法的事。

代码文件 get-tweets_by_AndyPatel.py 是 Andy Patel 在博文《How To Get Tweets From A Twitter Account Using Python And Tweepy》(https://labsblog.f-secure.com/2018/01/26/how-to-get-tweets-from-a-twitter-account-using-python-and-tweepy/) 的代码。
我改写的代码文件 retrieve-tweets-using-tweepy_by_litanid.NK.py 主要参考了这篇文章。

 retrieve-tweets-using-tweepy_by_litanid.NK.py 用 python3 编写，利用 tweepy 库连接 Twitter API 获取 tweets 。文件代码比较简单，一看即懂。

运行此文件，需要提供初始日期和结束日期，如：
`python3 retrieve-tweets-using-tweepy_by_litanid.NK.py 2018-01-01 2018-01-31`
则将获取北京时间2018年1月1日00:00:00至2018年1月31日23:59:59之间的推文数据，生成 2018-01-01-2018-01-31.js 文件，可以使用 extract-tweets (https://github.com/litanid/extract-tweets) 中的 extract-tweets-to-md_by_litanid_after.py 进行处理输出为 Markdown 文件。