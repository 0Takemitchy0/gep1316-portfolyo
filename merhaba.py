# merhaba.py
# Kullanıcının adını ve doğum yılını alıp yaşını hesaplayan,
# kişiye özel bir karşılama mesajı yazan program.

# datetime modülünü içe aktarıyoruz; bugünün tarihini öğrenmek için gerekli.
import datetime

# Kullanıcıdan adını istiyoruz; input() klavyeden yazılanı metin olarak döndürür.
ad = input("Adın ne? ")

# Kullanıcıdan doğum yılını istiyoruz; input() metin verdiği için int() ile sayıya çeviriyoruz.
dogum_yili = int(input("Hangi yıl doğdun? "))

# Bilgisayarın saatinden içinde bulunduğumuz yılı alıyoruz (ör. 2026).
bu_yil = datetime.date.today().year

# Bu yıldan doğum yılını çıkararak yaşı hesaplıyoruz.
yas = bu_yil - dogum_yili

# Ad ve yaşı kullanarak kişiye özel karşılama mesajını ekrana yazdırıyoruz.
# Baştaki f harfi, süslü parantez içindeki değişkenlerin metne yerleştirilmesini sağlar.
if dogum_yili > bu_yil:
    print("Gelecekten mi geldin? Doğum yılını kontrol et!")
else:
    print(f"Merhaba {ad}! Bu yıl {yas} yaşına giriyorsun. GEP1316'ya hoş geldin!")
  