def correctValue(ch):
    new = ""
    for c in ch:
        if c!='+' and c!='-':
            new+=c
        else : 
            break;
    return new
