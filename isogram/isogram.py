def is_isogram(string):
    s=string.upper()
    s_list=[]
    for l in s:
        if l.isalpha():
            if l in s_list:
                return False
            s_list.append(l)
    return True
   