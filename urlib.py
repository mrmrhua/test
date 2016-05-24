import urllib.request

weburl = "http://www.douban.com"

webheader = {'User-Agent':'Mozilla/5.0 ( Windows NT 6.1; WOW64; rv:23.0 ) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url=weburl, headers=webheader)  
webpage = urllib.request.urlopen(req)

data = webpage.read().decode('ascii', 'ignore')

# data = unicode(data,'utf-8')
# data = data.decode("ascii","ignore")
# print(data)

file = open("result.html", "w")
file.write(data)
file.close()
