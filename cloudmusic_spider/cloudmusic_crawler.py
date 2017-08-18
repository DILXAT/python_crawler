# 爬取网易云音乐的爬虫
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import urllib

#获取网页
def gethtml(url, headers={}):
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    content = response.read().decode('utf-8')
    response.close()
    return content

#解析音乐列表网页
def parsehtmlMusicList(html):
    soup = BeautifulSoup(html, 'lxml')
    list_pic = soup.select('ul#m-pl-container li div img')
    list_nameUrl = soup.select('ul#m-pl-container li div a.msk')
    list_num = soup.select('div.bottom span.nb')
    list_author = soup.select('a[class="nm nm-icn f-thide s-fc3"]')
    # n = 0
    length = len(list_pic)
    # while n < length:
    #     print('歌单图片：'+list_pic[n]['src']+'\n\n')
    #     print('歌单名称：'+list_nameUrl[n]['title']+'\n\n歌单地址：'+list_nameUrl[n]['href']+'\n\n')
    #     print('歌单播放量：'+list_num[n].text+'\n\n')
    #     print('歌单作者：'+list_author[n]['title']+'\n\n作者主页：'+list_author[n]['href']+'\n\n\n')
    #     n += 1
    return (list_pic,list_nameUrl,list_num,list_author,length)

url = 'http://music.163.com/discover/playlist'
url = gethtml(url, headers={
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'music.163.com'
})
datas=parsehtmlMusicList(url)
# print((parsehtmlMusicList(url)[0][0]['src']))


 # 在windows下新文件的默认编码是gbk，需手动改为utf-8
fout = open('output.html', 'w', encoding='utf-8')
fout.write('<html>')
fout.write('<body>')
fout.write('<table style=" border:1px solid black "">')
fout.write('<tr>')
fout.write('<th style=" border:1px solid black ">歌单图片</th>')
fout.write('<th style=" border:1px solid black ">歌单名称</th>')
fout.write('<th style=" border:1px solid black ">歌单地址</th>')
fout.write('<th style=" border:1px solid black ">歌单播放量</th>')
fout.write('<th style=" border:1px solid black ">歌单作者</th>')
fout.write('<th style=" border:1px solid black ">作者主页</th>')
fout.write('</tr>')
length_1=datas[4]

n=0
while n < length_1:
	fout.write('<tr>')
	fout.write('<td style=" border:1px solid black "><img src="%s" alt="" /></td>' % datas[0][n]['src'])
	fout.write('<td style=" border:1px solid black ">%s</td>' % datas[1][n]['title'])
	fout.write('<td style=" border:1px solid black ">http://music.163.com/#%s</td>' % datas[1][n]['href'])
	fout.write('<td style=" border:1px solid black ">%s</td>' % datas[2][n].text)
	fout.write('<td style=" border:1px solid black ">%s</td>' % datas[3][n]['title'])
	fout.write('<td style=" border:1px solid black ">http://music.163.com/#%s</td>' % datas[3][n]['href'])
	fout.write('</tr>')
	n += 1

fout.write('</table>')
fout.write('</body>')
fout.write('</html>')
fout.close()