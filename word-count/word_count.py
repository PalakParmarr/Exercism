import re
def count_words(sentence):
    sl=sentence.lower()
    word= re.sub('[^a-zA-Z0-9]','',sl).split()
    w_dict={    }
    for w in word:
        if w in w_dict:
            w_dict[w]+=1
        else:
            w_dict[w]+=1
    return w_dict