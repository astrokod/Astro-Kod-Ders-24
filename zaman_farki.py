from astropy.time import Time, TimeDelta

# zaman objesi oluştur
zaman = Time("2020-12-07T14:59:00", scale="utc", format="isot")

# Zaman objesini şimdi için oluştur (utc)
zaman2 = Time.now()

# Şimdi ve zaman objesinin farkını al
fark = zaman2 - zaman
print("Zaman farkı veri türü:", type(fark))
print("Gün kesiri cinsinden zaman farkı:", fark)
print("Saniye kesiri cinsinden zaman farkı:", fark.sec)

# Zaman farkı verisi oluştur, jd=Gün, sec=saniye
zaman_f = TimeDelta(1, format="jd")
# farkı saniye cinsinden göster
print(zaman_f.sec)

# Zaman2'ye zaman farkını ekle
print(zaman2 + zaman_f)

# zaman2'den başlayarak zaman_f aralıklarla 10 tane zaman objesi oluştur
print([zaman2 + zaman_f * i for i in range(10)])
