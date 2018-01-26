import sys
import io
import random

def main(src, n):
    """ """
    text = book_slice(src)
    dict = dict_create(text)
    new_builder(dict, n)

def book_slice(src):
    """ Read file, and import words from file into a long list """

    f = open(src, 'r', encoding='utf8')
    text = f.read()
    f.close()
    strip_text = []
    text = text.split()
    for word in text:
        strip_text.append(word.strip('.!()?_:-0123456789""'))
    return strip_text

def dict_create(text):
    """ Build dictionary with list of words from text """
    dict = {'': ['']}
    for i in range(0, len(text)):
        if i < len(text) - 2:
            if text[i] + " " + text[i+1] not in dict:
                dict[text[i] + " " + text[i+1]] = [text[i+2]]
            else: 
                dict[text[i] + " " + text[i+1]] = dict[text[i] + " " + text[i+1]] + [text[i+2]]
    return dict

def new_builder(dict, n):
    """ Create a few paragraphs (words = n) of a 'story' from the dictionary """
    dict_keys = list(dict.keys())
    start = random.choice(dict_keys)
    prose = start.split()
    prose.append(random.choice(dict[start]))
    for i in range(1,n):
        prose.append(random.choice(dict[prose[i] + " " + prose[i + 1]]))
    paragraph = ' '.join(prose)
    print(paragraph)

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))

# main('moby_dick.txt', 200)