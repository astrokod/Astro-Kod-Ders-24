from astropy.time import Time
# Zaman tanımla
zaman = Time("2020-12-07T14:54:00", scale="utc", format="isot")

# Zaman Formatını değiştir
print(zaman.iso)
print(zaman.to_value("jd"))

# zamanı mevcut bütün formatlarda göster
for frmt in Time.FORMATS.keys():
    print(frmt, zaman.to_value(frmt))
