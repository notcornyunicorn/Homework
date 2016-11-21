import os
import re

def first_task():
    d = {}
    directory = r'C:\Users\student\Desktop\тайский'
    files = os.listdir(directory)
    regex_value = r"<td class=pos>.+?</td><td>(.+?)</td>"
    regex_key = r"<td class=th><a href='/id/.+?'>(.+?)</a>"
    for file in files:
        f = open(file, 'r', encoding = 'utf-8')
        text = f.read()
        f.close()
        result_key = re.search(regex_key, text)
        key = result_key.group(1)
        result_value = re.search(regex_value, text)
        value = result_value.group(1)
        d[key] = value
    return d

def main():
    first = first_task()
       
if __name__=='__main__':

    main()
