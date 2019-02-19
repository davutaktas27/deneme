defkullanıcı="davut1"
defsifre="123456"

while True:
    kullanıcı=input("kullanıcı adı: ")
    sifre=input("sifre girin")
    if(defkullanıcı!=kullanıcı or defsifre!=sifre):
        print("Bilgiler yanlış..")
    else:
        print("Hoşgeldiniz...")
        break

listeler=[3,4]

for i in range(1,10):
    if(i in listeler):
        continue
    print(i)
    #continue sonsuz döngü hatası verebilir.