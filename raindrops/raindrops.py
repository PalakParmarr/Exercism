def convert(number):
    r = ""

    if number % 3 == 0:
        r = r +"Pling"
    elif number % 5 == 0:
        r = r + "Plang"
    elif number % 7 == 0:
        r=r +"Plong"
    elif number%5 != 0 and number%3 !=0 and number%7 !=0:
        r = str(number)
    return  r
