from urllib import request
url ='http://baidu.com'
print('第一种方法')
response_1=request.urlopen(url)
print(response_1.getcode())
print(len(response_1.read())