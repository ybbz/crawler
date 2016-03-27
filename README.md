# crawler

This is a crawler, you can use it to crawl resources.

### get_html_img

Download all the images of a web page.

### crawl_weibo

* Crawl all the text of your Weibo account, and write the result to the document.
* Cut the text result of your weibo with jieba, so you can get your words list of Weibo.
* read stopwords.txt, get stop words list;remove all stop words of step2, get the new words list
* Statistics frequency of the new word list, get the list of frequency.
* Sort the result of step4, then, get top30 words.
* Draw the picture of your top30 words.
