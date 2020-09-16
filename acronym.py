def abbreviate(words):
    list=words.replace("_", "").replace("-", " ").split()
    str= ""
    for x in list:
        str+=x[0]
        str=str.upper()
    return str