# urllib2 

> python2.7

> python 自带的模块 抓取http资源的模块

```py

    # coding=utf8

    import urllib2


    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
    }

    # 构造一个请求对象
    request = urllib2.Request("http://www.baidu.com/",headers=headers)

    response = urllib2.urlopen(request)

    html = response.read()

    print html

```

User-Agent： 爬虫与反爬虫原理第一步