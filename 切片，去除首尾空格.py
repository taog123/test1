def trim(str):
    while str[:1]==' ':
            str = str[1:]
    while str[-1:] == ' ':
            str = str[:-2]
    return str
print(trim('   abc hh welome!       '))