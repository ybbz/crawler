"""
- Crawl all articles including title and time from Categories page of your blog.
- Analyze the data above and save result to database(title、create_time、content...）.
- Query data from database and show your articles(to be continued).
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import mysql.connector

url = 'http://blog.ybbz.site/Categories/'
html = urlopen(url)
bsObj = BeautifulSoup(html, 'lxml')
uls = bsObj.findAll('ul', {'class': 'listing'})
cate_list = []
for ul in uls:
    cate = ul.h4.string
    for li in ul.findAll('li'):
        cate_list.append((str(cate), str(li.time.string), str(li.a.string)))
print(cate_list)

host = 'your hostname'
user = 'your username'
passwd = 'your password'
db = 'your database'
# connect database
conn = mysql.connector.connect(host=host, user=user, passwd=passwd, db=db)
cursor = conn.cursor()
# save blogs
sql = "insert into blog(category,create_time,title) values(%s, %s, %s)"
cursor.executemany(sql, cate_list)
conn.commit()
