def response(hey_bob):
    hb=hey_bob.strip()
    if hey_bob.isupper() and hey_bob.endswith('?'): 
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper(): 
        return 'Whoa, chill out!'
    elif hey_bob.endswith('?'): 
        return 'Sure.'
    elif not hb: 
        return 'Fine. Be that way!'
    else:	
        return 'Whatever.'