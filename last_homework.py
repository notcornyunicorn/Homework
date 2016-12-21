import os

def reading(filename):
    f = open(filename, 'r', encoding = 'utf-8')
    a = f.read()
    a = a.split()
    f.close()
    text = []
    for word in a:
        if  word.endswith('.') or word.endswith(',') or word.endswith(':'):
            text.append(word[:-1])
            text.append(word[-1:])
        else:
            text.append(word)
    f = open('C:\\Users\\M_Nastya\\Desktop\\proga\\example\\example.txt', 'a', encoding = 'utf-8')
    for word in a:
        f.write(word + '\n')
    f.close()
    return text

def stemming():
    inp = 'C:\\Users\\M_Nastya\\Desktop\\proga\\example'
    lst = os.listdir(inp)
    for fl in lst:
        line = 'C:\\mystem.exe -n ' + inp + os.sep + fl + ' C:\\Users\\M_Nastya\\Desktop\\proga\\result' + os.sep + fl
        os.system(line)
    f = open('C:\\Users\\M_Nastya\\Desktop\\proga\\result\\example.txt', 'r', encoding = 'utf-8')
    a = f.read()
    a = a.split('}')
    f.close()
    d = {}
    for word in a:
        word = word.strip('\n')
        word = word.split('{')
        for element in word:
            d[word[0]] = element
    return d

def tabling(text, d):
    a = []
    for word in text:
        if word.isalpha():
            a.append(word)
    f = open('C:\\Users\\M_Nastya\\Desktop\\proga\\комманды.txt', 'a', encoding = 'utf-8')
    i = 0
    for word in a:
        id_number = str(i)
        wordform = word.lower()
        lemma = d[word]
        number_in_text = str(i + 1)
        id_lemma = str(i)
        first_command = "INSERT INTO table (id, wordform, lemma) VALUES ('"+ id_number + "', '" + wordform + "', '" + lemma + "');\n"
        second_command = "INSERT INTO table (id, wordform, number_in_text, id_lemma) VALUES ('"+ id_number + "', '" + wordform + "', '" + number_in_text + "', '" + id_lemma + "');\n"
        i += 1
        command = first_command + second_command
        f.write(command)
    f.close()

def main():
    text = reading('C:\\Users\\M_Nastya\\Desktop\\proga\\текст.txt')
    lemmas = stemming()
    tables = tabling(text, lemmas)
    
if __name__=='__main__':
    main()

