# GEP1316 Kodlama Okuryazarlığı - Ödev 3
# Mobil Oyun LTV (Oyuncu Başına Yaşam Boyu Değer) Hesaplayıcı
#
# Formüller:
#   LTV       = ARPDAU x ortalama oyuncu ömrü (gün)
#   Net Kâr   = LTV - CPI
#   ROI (%)   = (Net Kâr / CPI) x 100

# --- 1) Kullanıcıdan girdileri alma ---

# Oyunun adı metin olarak alınır (str veri tipi)
oyun_adi = input("Oyunun adı: ")

# input() her zaman metin döndürür; ondalıklı sayı için float() ile dönüştürüyoruz
arpdau = float(input("Günlük aktif oyuncu başına ortalama gelir (ARPDAU, $): "))

# Gün sayısı tam sayı olduğu için int() ile dönüştürüyoruz (int veri tipi)
oyuncu_omru_gun = int(input("Bir oyuncunun oyunda ortalama kaldığı gün sayısı: "))

# Bir oyuncuyu reklamla kazanmanın maliyeti de ondalıklı olabilir (float veri tipi)
cpi = float(input("Oyuncu başına edinme maliyeti (CPI, $): "))

# --- 2) Girdi kontrolü ---

# Negatif değerler anlamsız olduğu için karşılaştırma operatörleriyle kontrol ediyoruz
girdiler_gecerli = arpdau >= 0 and oyuncu_omru_gun >= 0 and cpi >= 0  # bool veri tipi

if not girdiler_gecerli:
    print("Hata: Girilen değerler negatif olamaz. Lütfen programı tekrar çalıştırın.")
else:
    # --- 3) Hesaplamalar (aritmetik operatörler) ---

    # Bir oyuncunun oyuna toplamda kazandırdığı gelir
    ltv = arpdau * oyuncu_omru_gun

    # Oyuncu başına kâr ya da zarar
    net_kar = ltv - cpi

    # Reklam harcamasının kârlı olup olmadığı (bool veri tipi)
    karli_mi = net_kar > 0

    # --- 4) Sonuçları f-string ile biçimli yazdırma ---

    print()
    print(f"===== {oyun_adi} için LTV Raporu =====")
    print(f"Oyuncu başına yaşam boyu değer (LTV): ${ltv:.2f}")
    print(f"Oyuncu edinme maliyeti (CPI):        ${cpi:.2f}")
    print(f"Oyuncu başına net kâr/zarar:          ${net_kar:.2f}")

    # CPI sıfırsa bölme hatası olmaması için ROI'yi yalnızca CPI > 0 iken hesaplıyoruz
    if cpi > 0:
        roi = net_kar / cpi * 100
        print(f"Reklam yatırımının getirisi (ROI):    %{roi:.1f}")
    else:
        print("ROI hesaplanamadı: CPI sıfır (ücretsiz edinilen oyuncu).")

    # Kârlılık durumuna göre farklı mesaj gösterme
    if karli_mi:
        print("Sonuç: Reklam harcaması KÂRLI. Her yeni oyuncu para kazandırıyor.")
    elif net_kar == 0:
        print("Sonuç: Başa baş. Reklam harcaması ancak kendini çıkarıyor.")
    else:
        print("Sonuç: Reklam harcaması ZARARDA. Oyuncu kazandırdığından pahalıya geliyor.")
