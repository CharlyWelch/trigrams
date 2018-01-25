def main(src, numwords):
    """ """
    book_slice(src)

def book_slice(src):
    """ Function to read file, and import words from file into a long list """
    import io

    f = open(src, 'r')
    text = f.read()
    f.close()
    return text.split()

def dict_create(text):
    """ Build dictionary with list of words from text """
    dict = {'can can': ['can']}
    for i in range(0, len(text)):
        if i < len(text) - 2:
            if text[i] + " " + text[i+1] not in dict:
                dict[text[i] + " " + text[i+1]] = [text[i+2]]
            else: #key does exist, add value to list of values:
                dict[text[i] + " " + text[i+1]] = dict[text[i] + " " + text[i+1]] + [text[i+2]]
    return dict

book = book_slice('whitman.txt')
print(book)
print(dict_create(book))
