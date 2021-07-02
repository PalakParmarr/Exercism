import re

def abbreviate(words):

   word = re.findall(r"[A-Za-z']+", words.upper())
   return "".join(w[0] for w in word)