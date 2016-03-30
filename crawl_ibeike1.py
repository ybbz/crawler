# encoding=utf-8

import httplib2
import mysql.connector
from bs4 import BeautifulSoup

result = []
pageNum = 'total page number'
uid = 'your uid'
cookie = "your cookies"

url = 'http://city.ibeike.com/home.php?mod=space&uid=' + uid + '&do=thread&view=me&order=dateline&from=space&page='

headers = {"Connection": "keep-alive",
           "Cookie": cookie,
           "Content-Type": "application/xhtml+xml"}

for page in range(1, pageNum + 1):
    cur_page = page
    url_full = url + str(cur_page)
    # http request
    http = httplib2.Http()
    response, content = http.request(url_full, "GET", headers=headers)
    if response.status == 200:
        # print(response)
        # print(content.decode('utf-8'))
        soup = BeautifulSoup(content, "lxml")
        table = soup.find_all('table')[1]
        tr = table.find_all('tr', class_='')
        for item in tr:
            item_list = []
            # print(item.prettify())
            item_title = item.th.a.string
            item_group = item.find_all('td', class_='')[0].a.string
            item_reply = item.select('td[class="num"]')[0].a.string
            item_watch = item.select('td[class="num"]')[0].em.string
            # save to the result list
            item = (str(item_title), str(item_group), int(item_reply), int(item_watch))
            result.append(item)
print(result)

# connect database
conn = mysql.connector.connect(host="hostname", user="username", passwd="password", db="database")
cursor = conn.cursor()
# save data
sql = "insert into ibeike(title,groups,reply,watch) values(%s,%s,%s,%s)"
cursor.executemany(sql, result)
conn.commit()
