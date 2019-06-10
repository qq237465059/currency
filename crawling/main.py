# -*- coding:UTF-8 -*-
import time

from crawling.baseSpider.html_DownLoad import HtmlDownLoad
from crawling.baseSpider.url_Manage import UrlManage
from crawling.regulation.html_Perser_Url import HtmlPerserUrl
from crawling.output.PrintDatabase import PrintDatabase

if __name__ == "__main__":
    print("start")
    baseUrl = "https://www.amazon.com/"
    url = "https://www.amazon.com/"
    # 实例化html下载
    download = HtmlDownLoad()
    # url管理器
    manager = UrlManage()
    # 添加电子产品的url管理器
    electronics = "https://www.amazon.com/s/browse?_encoding=UTF8&node=16225009011&ref_=nav_shopall-export_nav_mw_sbd_intl_electronics&language=zh_CN"
    manager.add_new_url(electronics)
    # 定义一个储存商品url的管理器
    products = UrlManage()
    # 首先发送post请求， 将界面变为中文
    # download.checkLanguage(url)

    # 储存
    database = PrintDatabase()

    # size
    size = 10
    i = 0
    while i < size:
        if manager.has_new_url():
            url = manager.get_new_url()
        else:
            if i > 0 and not manager.has_new_url():
                break
        # 下载html
        print(url)
        content = download.DownLoad(url)
        # 解析HTML内容获取需要的内容

        # 解析URL,获取当页的商品
        productUrls = HtmlPerserUrl.parseProductUrls(baseUrl, content)
        products.add_new_urls(productUrls)
        # 获取下一页的按钮，并补全添加到url存储
        urls = HtmlPerserUrl.parseUrl(baseUrl, content)
        # 储存
        manager.add_new_url(urls)

        i = i + 1

    print("-----------------------------------------------------------------------------------")
    # while products.has_new_url():
    #     print(products.get_new_url())
    # size
    while products.has_new_url():
        url = products.get_new_url()
        print(url)
        content = download.DownLoad(url)
        map = HtmlPerserUrl.parseHtml(content)
        if 'productName' not in map.keys():
            continue
        map["url"] = url
        map["created"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # print("1")
        database.save(map, "product")

    download.closeBrowser()
    print("end")

