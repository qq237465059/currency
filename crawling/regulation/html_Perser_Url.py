# -*- coding:UTF-8 -*-

from bs4 import BeautifulSoup


class HtmlPerserUrl(object):

    @staticmethod
    def urljoin(page_url, old_url):
        url = '%s/%s' % (page_url, old_url)
        return url

    @staticmethod
    def parseUrl(page_url, html_content):
        url = ""
        soup = BeautifulSoup(html_content, "html.parser")
        # soup = BeautifulSoup(html_content, "html5lib")
        try:
            tag = soup.select('a[id="pagnNextLink"]')[0]
            href = tag['href']
        except:
            try:
                tags = soup.select('li[class="a-last"]')
                href = tags[0].select('a')[0]["href"]
            except:
                1

        if href.startswith('/'):
            url = HtmlPerserUrl.urljoin(page_url, href)
        return url

    @staticmethod
    def parseProductUrls(page_url, html_content):
        urls = set()
        soup = BeautifulSoup(html_content, "html.parser")
        # soup = BeautifulSoup(html_content, "html5lib")
        tags = soup.select('li')
        for tag in tags:
            try:
                divs = tag.select('div[class="a-row a-spacing-none"]')
                for div in divs:
                    try:
                        href = div.select('a')[0]["href"]
                        if href.startswith('/'):
                            href = HtmlPerserUrl.urljoin(page_url, href)
                        urls.add(href)
                    except:
                        continue
            except :
                continue
        tags = soup.select('div[class="sg-col-inner"]')
        for tag in tags:
            try:
                divs = tag.select('div[class="sg-row"]')
                for div in divs:
                    try:
                        href = div.select('a')[0]["href"]
                        if href.startswith('/'):
                            href = HtmlPerserUrl.urljoin(page_url, href)
                        urls.add(href)
                    except:
                        continue
            except :
                continue
        return urls

    @staticmethod
    def parseHtml(html_content):
        map = {}
        soup = BeautifulSoup(html_content, "html.parser")
        # soup = BeautifulSoup(html_content, "html5lib")
        try:
            tag = soup.select('span[id="productTitle"]')[0]
            title = tag.text.strip()
            print(title)
            tag = soup.select('span[id="priceblock_ourprice"]')[0]
            price = tag.text.strip()
            print(price)
            map["productName"] = title
            map["price"] = price
        except:
            1
        return map

