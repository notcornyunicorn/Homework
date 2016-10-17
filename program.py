import urllib.request
import re
import html
import os

def newspaper():
    os.makedirs(r'C:\Users\M_Nastya\Desktop\Учеба\Программирование\Newspaper')
    topics = ['society', 'news', 'official', 'policy', 'economic', 'accidents', 'culture', 'sport']
    for i in range(1, 123249):
        for topic in topics:
            articlename = 'http://vecherka.su/articles/' + topic + '/' + str(i) + '/'
            req = urllib.request.Request(articlename)
            with urllib.request.urlopen(req) as response:
                text = response.read().decode('utf-8')
                if 'errortext' not in text and '<span class=\"link\">' in text:
                    data = interpretator(text)    
                    break
    return text

def interpretator(text):
    regex = re.compile('<span class=\"link\">\n(.*?)</span>')
    au = regex.findall(text)
    author_name = au[0]
    author_name = author_name.strip()
    print(author_name)
    regex = re.compile('<title>(.*?)</title>')
    ti = regex.search(text)
    title_name = ti.group(1)
    title_name = title_name[:-20]
    regex = re.compile('<div class="date">\n(.*?)- автор')
    da = regex.search(text)
    date_name = da.group(1)
    date_name = date_name.strip()
    date_name = date_name[:10]
    month = date_name[3:5]
    year = date_name[6:]
    regex = re.compile('<a href="/articles/(.*?)/" class="current">(.*?)</a>')
    to = regex.search(text)
    topic_name = to.group(2)
    regex = re.compile('<meta property="og:url" content="(.*?)" />')
    ur = regex.search(text)
    url_name = ur.group(1)
    regex = re.compile('<div class="detail-text">(.*?)</div>', flags=re.U | re.DOTALL)
    na = regex.search(text)
    naked_text_result = na.group(1)
    naked_text_result = html.unescape(naked_text_result)
    regex = '<br />'
    sub = ''
    naked_text_result = re.sub(regex, sub, naked_text_result)
    regex1 = '\t\t\t'
    naked_text_result = re.sub(regex1, sub, naked_text_result)
    return author_name, title_name, date_name, month, year, topic_name, url_name, naked_text_result
       
def main():
    text = newspaper()    
    
if __name__=='__main__':
    main()
