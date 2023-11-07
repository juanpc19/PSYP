#no hay que indicar tipo parametro entrada en python
def esVocal(letra):
    vocal=False
    
    if letra in ["a","e","i","o","u"]:
        vocal=True
    else:
        vocal=False
             
    return vocal