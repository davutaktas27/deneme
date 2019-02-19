def topla(liste):
    toplam=0
    for i in liste:
        toplam+=i
    return toplam
liste=[7,6,5]

print(topla(liste))

def recursif(liste):
    if len(liste)==0:
        return 0
    else:
        return liste[0]+ recursif(liste[1:])

print("recursif",recursif([3,6,8]))

#yerel ve global değişkenler
a=10
b=13
def fonka():

    global b
    b=6
    b=8
    a=8
    print("Yerel a= b=",a,b)
print("Global a=  b=",a,b)
fonka()
print("Global a=  b=",a,b)