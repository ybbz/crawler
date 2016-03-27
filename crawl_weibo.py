# encoding=utf-8

import requests
from lxml import etree
import jieba
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

result = ''
count = 1
user_id = your weibo user_id
cookie = {"Cookie": your weibo cookie}
download_path = '/Users/ybbz/Downloads/weibo/'

print('crawl the text of your weibo: start...')

# get total page number
html = requests.get('http://weibo.cn/%d/profile?page=1' % user_id, cookies=cookie).content
selector = etree.HTML(html)
pageNum = int((selector.xpath('//input[@name="mp"]')[0].attrib['value']))

# crawl your weibo
for page in range(1, pageNum + 1):
    # for page in range(1, 2):
    # get lxml
    url = 'http://weibo.cn/%d/profile?page=%d' % (user_id, page)
    lxml1 = requests.get(url, cookies=cookie).content
    # get text
    selector = etree.HTML(lxml1)
    content = selector.xpath('//span[@class="ctt"]')
    for each in content:
        text = each.xpath('string(.)')
        text = "%d :" % count + text + "\n"
        result += text
        count += 1

# write the result to the document
with open(download_path + str(user_id), 'w') as f:
    f.write(result)

print('crawl : done, a total of %d data.' % (count - 1))
######################################################
print('analyze the text of your weibo : start...')

stop_list = []
word_list = []
word_dict = {}
word_frequency = []

file_stopwords = 'stopwords.txt'

# read stopwords.txt,get stop words list
with open(file_stopwords, 'r') as f_stop:
    f_stop_text = f_stop.read()
    stop_list = f_stop_text.split('\n')

# cut the text result of your weibo with jieba
result_cut = jieba.cut_for_search(result)

# remove all stop words,get the new word list
for cut in result_cut:
    if not (cut.strip() in stop_list):
        word_list.append(cut)

# statistics frequency of the new word list
for word in word_list:
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

# get the list of frequency
for key in word_dict:
    word_frequency.append((word_dict[key], key))

# sort the result and get top 20
word_20 = sorted(word_frequency)[-30:]
word_20.reverse()

print('analyze : done.')
######################################################
print('draw : start...')

csv_path = '/Users/ybbz/Downloads/weibo/weibo.csv'

# write top30 result to csv document
with open(csv_path, 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(['frequency', 'word'])
    f_csv.writerows(word_20)

# read data and draw picture
budget = pd.read_csv(csv_path)
sns.set_style("darkgrid")
bar_plot = sns.barplot(x=budget["word"], y=budget["frequency"], palette="muted", order=budget["word"].tolist())
plt.xticks(rotation=0)
plt.show()

print('draw : done.')
