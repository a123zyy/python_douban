# -*- coding: UTF-8 -*-
#
import re
import urllib2

import xlwt
from bs4 import BeautifulSoup

findLink = re.compile(r'<a class="" href="(.*?)"')
title = re.compile(r'<a.*title="(.*?)">')
time = re.compile(r'<td class="td-time" nowrap="nowrap" title="(.*?)"')


# 爬取网页内容
def askUrl(url):
    head = {
        "User-Agent": " Mozilla/4.0 (Macintosh; Intel Mac OS X 10_15_8) AppleWebKit/537.0 (KHTML, like Gecko) Chrome/98.80 Safari/537.0"}
    request = urllib2.Request(url, headers=head)
    try:
        response = urllib2.urlopen(request)
        html = response.read().decode("utf-8")
        return html
    except urllib2.HTTPError as e:
        print(e)
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)


# 存入excel
def saveData(___list___, name):
    print("save....")
    workBook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = workBook.add_sheet('豆瓣租房', cell_overwrite_ok=True)
    col = ("title", "href", "time")
    for i in range(0, 3):
        sheet.write(0, i, col[i])
    for j in range(0, len(list)):
        print("第" + str(j) + "条")
        data = list[j]
        for k in range(0, 3):
            sheet.write(j + 1, k, data[k])
    workBook.save(name)
    return None


#
def getData(url, area):
    datalist = []
    # range(0,8) 这个循环量取决于有多少页
    for i in range(0, 8):
        page = str(i * 50)
        url = url + "start=" + page + "&cat=1013&group=146409&sort=time&q=" + str(area)
        html = askUrl(url)
        # 解析爬取内容
        soup = BeautifulSoup(html, "html.parser")
        # 截取到想要的内容
        for item in soup.find_all('tr', class_="pl"):
            data = []
            item = str(item)
            tr_title = re.findall(title, item)
            data.append(tr_title)
            tr_href = re.findall(findLink, item)[0]
            data.append(tr_href)
            tr_time = re.findall(time, item)[0]
            data.append(tr_time)
            datalist.append(data)
    return datalist


if __name__ == "__main__":
    baseurl = "https://www.douban.com/group/search?"  # 豆瓣小组链接
    list = getData(baseurl, "桂林路")
    saveData(list, "douban.xls")
