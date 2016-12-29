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
    f = open(r'C:\Users\student\Desktop\exam\cyrillic\c.txt', 'a', encoding = 'utf-8')
    for word in c:
        print(word)
        f.write(word + '\n')
    f.close()
    return c

def second_task(c):
    inp = r'C:\Users\student\Desktop\exam\cyrillic'
    lst = os.listdir(inp)
    for fl in lst:
        line = r'C:\mystem.exe -i ' + inp + os.sep + fl + r' C:\Users\student\Desktop\exam\verbs' + os.sep + fl
        os.system(line)
    f = open(r'C:\Users\student\Desktop\exam\verbs\c.txt', 'r', encoding = 'utf-8')
    stemmed_words = f.read()
    stemmed_words = stemmed_words.split('}')
    verbs = []
    for word in stemmed_words:
        if '=V' in word:
            verbs.append(word)
    clean_verbs = []
    for verb in verbs:
        word = verb.split('{')
        clean_verbs.append(word[0])
    for verb in clean_verbs:
        print(verb)

def third_task():
    f = open(r'C:\Users\student\Desktop\exam\verbs\c.txt', 'r', encoding = 'utf-8')
    a = f.read()
    a = a.split('}')
    f.close()
    f = open(r'C:\Users\student\Desktop\exam\sql.txt', 'a', encoding = 'utf-8')
    regex = '([а-я]+?)\?*=([A-Z])+'
    i = 0
    for word in a:
        id_number = i
        word = word.split('{')
        wordform = word[0]
        gram = word[1]
        result = re.findall(regex, gram)
        lemma = result[0]
        part_of_speech = result[1]
        command = "INSERT INTO table (id, wordform, lemma, part of speech) VALUES ('"+ id_number + "', '" + wordform + "', '" + lemma + "', '" + part_of_speech + "');\n"
        f.write(command + '\n')
        i += 1
    f.close()


def main():
    html = download_page(r'http://web-corpora.net/Test2_2016/short_story.html')
    text = words(html)
    c = first_task(text)
    verbs = second_task(c)
    insert = third_task()
    
       
if __name__=='__main__':
    main()
