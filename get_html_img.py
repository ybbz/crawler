from urllib import request, parse
import re

def get_html_img(url):
    req = request.Request(url)
    with request.urlopen(req) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        content = f.read()
        print('Content:', content)
        body = re.findall('<body>(.*?)</body>', str(content), re.S)
        img_urls = re.findall('src="(.*?)"', str(body), re.S)
        count = 1
        local_dir = '/Users/Downloads/'
        print("download images start ……")
        for img_url in img_urls:
            img_url_full = url + img_url
            # 下载图片
            local_name = local_dir + str(count) + '.jpg'
            count += 1
            try:
                request.urlretrieve(img_url_full, local_name)
            except Exception as e:
                continue
        print("download images success !")

url = 'http://www.xxx.com'
get_html_img(url)
