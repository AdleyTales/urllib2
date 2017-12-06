# coding=utf8

import urllib2

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
}

# 构造一个请求对象
request = urllib2.Request("http://www.baidu.com/",headers=headers)

response = urllib2.urlopen(request)

html = response.read()

# 响应码
code = response.getcode()

# 具体返回的url，防止重定向
true_url = response.geturl()

# 返回服务器响应报头信息
info = response.info()


# print html

print code #200

print true_url # https://www.baidu.com/

print info 

# Bdpagetype: 1
# Bdqid: 0xd6bbee040001a4c6
# Bduserid: 0
# Cache-Control: private
# Content-Type: text/html; charset=utf-8
# Cxy_all: baidu+8db55f0632d9a4253e774a5873af2b2d
# Date: Wed, 06 Dec 2017 14:59:30 GMT
# Expires: Wed, 06 Dec 2017 14:58:47 GMT
# P3p: CP=" OTI DSP COR IVA OUR IND COM "
# Server: BWS/1.1
# Set-Cookie: BAIDUID=6DFDE6C7B12859C88C1BB4DB9809CF9D:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
# Set-Cookie: BIDUPSID=6DFDE6C7B12859C88C1BB4DB9809CF9D; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
# Set-Cookie: PSTM=1512572370; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com

# Set-Cookie: BDSVRTM=0; path=/
# Set-Cookie: BD_HOME=0; path=/
# Set-Cookie: H_PS_PSSID=1444_21124_18560_25178_22074; path=/; domain=.baidu.com
# Strict-Transport-Security: max-age=172800
# Vary: Accept-Encoding
# X-Powered-By: HPHP
# X-Ua-Compatible: IE=Edge,chrome=1
# Connection: close
# Transfer-Encoding: chunked