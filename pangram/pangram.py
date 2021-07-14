def is_pangram(sentence):
    s= sentence.lower()
    a='abcdefghijklmnopqrstuvwxyz'

    for ch in a:
        if ch not in s :
            return False
    return True