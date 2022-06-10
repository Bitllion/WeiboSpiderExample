# WeiboSpiderExample
本文为 https://github.com/Python3Spiders/WeiboSuperSpider 的实现案例，爬取微博话题“东航坠机”，获得数据，再分别用 jieba 中文分词、snownlp 情感分析 、matplotlib绘制图片

# start
## 1.获取COOKIE
登录weibo.com, 可以通过F12抓包到用户COOKIE，我使用chrome插件 Get Cookie Plus 提取的
## 2.配置json
将cookie 填入 topic下的json 文件对应位置中，并设置关键词，时间范围，python=3.6.6 (必须)，pychram 运行test.py即可爬取
## 3.数据分析
分别运行项目主页三个py文件即可得到相应数据，数据保存再data目录下
