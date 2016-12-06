import urllib.request
import re
import html

def download():
    f = open('yandex.txt', 'r', encoding = 'utf-8')
    links = f.readlines()
    f.close()
    htmls = []
    for link in links:
        req = urllib.request.Request(link)
        with urllib.request.urlopen(req) as response:
            htmls.append(response.read().decode('utf-8'))
    return htmls

def texts(htmls):
    articles = []
    for text in htmls:
        regex = '<div class="(main-article|j-bp-150x50-article-top article__head__banner|b-article__text|content-note).*?">(.*?)<div class="(tags|article__source|b-article__related|post-page-content-tags)">'
        result = re.search(regex, text, flags=re.DOTALL)
        articles.append(result.group(2))
    regdiv = '<div.*?</div>'
    regblock = '<blockquote.*?>.*?</blockquote>'
    regtags = '</?(a|p|iframe|strong|b|script|h1|img|div).*?>'
    regbr = '<br/?>'
    articles_cl = []
    for text in articles:
        text = re.sub(regdiv, '', text, flags=re.DOTALL)
        text = re.sub(regblock, '', text, flags=re.DOTALL)
        text = re.sub(regtags, '', text, flags=re.DOTALL)
        text = re.sub(regbr, '', text, flags=re.DOTALL)
        text = re.sub('(\s)+', r'\1', text)
        text = html.unescape(text)
        text = re.sub('[a-zA-Z0-9_/.]*?\.(com|ru)/[a-zA-Z0-9_/.]*?[ .]', ' ', text)
        articles_cl.append(text)
    return articles_cl

def dicts(texts):
    worddicts = []
    for text in texts:
        words = text.split()
        worddict = {}
        for word in words:
            w = word.strip('.,?!:0123456789()"«»-–+/').lower()
            if w != '':
                if w in worddict:
                    worddict[w] += 1
                else:
                    worddict[w] = 1
        worddicts.append(worddict)
    return worddicts

def main():
    htmls = download()
    articles = texts(htmls)
    worddicts = dicts(articles)
    wordsets = [set(worddict) for worddict in worddicts]
    intersectionsets = wordsets[0]
    i = 1
    while i < 4:
        intersectionsets = intersectionsets.intersection(wordsets[i])
        i += 1
    i = 0
    diffs = []
    while i < 4:
        j = 0
        diffs.append(wordsets[i])
        while j < 4:
            if j == i:
                j += 1
            else:
                diffs[i] = diffs[i].difference(wordsets[j])
                j += 1
        i += 1
    symdifferencesets = diffs[0]
    i = 1
    while i < 4:
        symdifferencesets = symdifferencesets.union(diffs[i])
        i += 1
    symdifferencearr = list(symdifferencesets)
    symdifferencearr.sort()
    intersectionarr = list(intersectionsets)
    intersectionarr.sort()
    with open('intersection.txt', 'w', encoding='utf-8') as f:
        for word in intersectionarr:
                f.write(word + '\n')
    with open('symdifference.txt', 'w', encoding='utf-8') as f:
        for word in symdifferencearr:
                f.write(word + '\n')
    with open('symdifference2.txt', 'w', encoding='utf-8') as f:
        for word in symdifferencearr:
            for worddict in worddicts:
                if word in worddict and worddict[word] > 1:
                    f.write(word + '\n')
                    break
    
    
if __name__=='__main__':
    main()
