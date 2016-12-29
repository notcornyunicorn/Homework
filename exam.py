import urllib.request
import re
import os

def download_page(pageUrl): 
    req = urllib.request.Request(pageUrl)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    return html

def words(html):
    regex = '(([А-Я]|[а-я])[а-я]*)'
    html = re.findall(regex, html)
    text = []
    for array in html:
        text.append(array[0])
    return text

def first_task(text):
    c = []
    for word in text:
        if word.startswith('с') or word.startswith('С'):
            c.append(word)
    for word in c:
        print(word)
    return c

def second_task(c):
    inp = 'C:\\Users\\M_Nastya\\Desktop\\proga\\example'
    lst = os.listdir(inp)
    for fl in lst:
        line = 'C:\\mystem.exe -i ' + inp + os.sep + fl + ' C:\\Users\\M_Nastya\\Desktop\\proga\\result' + os.sep + fl
        os.system(line)

    
    
    




def main():
    html = download_page(r'http://web-corpora.net/Test2_2016/short_story.html')
    text = words(html)
    c = first_task(text)
    verbs = second_task(c)
    
       
if __name__=='__main__':
    main()
