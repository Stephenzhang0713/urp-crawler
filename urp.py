# coding=utf-8
import urllib,urllib2,cookielib

# hosturl用于获取cookies, posturl是登陆请求的URL
hosturl = 'http://jw.hhuwtian.edu.cn/'
posturl = 'http://jw.hhuwtian.edu.cn/loginAction.do'

# 获取cookies
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)
h = urllib2.urlopen(hosturl)

# 伪装成浏览器，反“反爬虫”——虽然我们学校的URP好像没有做反爬虫
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.1 Safari/605.1.15',
    'Referer':'http://jw.hhuwtian.edu.cn/'}
# 构造POST数据 用户名和密码，，自行修改啊，，别乱来啊。
postData = dict(dllx='dldl', zjh='150310136', mm='199607138')
postData = urllib.urlencode(postData)
# 构造请求
request = urllib2.Request(posturl, postData, headers)
# 登陆
urllib2.urlopen(request)
# 用一个方案成绩做测试
testurl = 'http://jw.hhuwtian.edu.cn/bxqcjcxAction.do?type=ln&oper=fainfo&fajhh=3792'
head = '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
save = head + urllib2.urlopen(testurl).read().decode('GBK').encode('UTF-8')
open('score.html', "w").write(save)